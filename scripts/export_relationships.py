"""Deterministically export the relationship stores into portable text files.

The canonical sources are ``data/knowledge.duckdb`` and ``data/chroma``.
NetworkX is rebuilt with the production graph builder so its export represents
the exact runtime graph.  Large datasets are written as JSON Lines to keep the
export streamable and independently verifiable.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import math
import os
import re
import shutil
import sys
import tempfile
import uuid
from collections import Counter
from collections.abc import Iterable, Iterator, Mapping, Sequence
from datetime import UTC, date, datetime, time
from decimal import Decimal
from pathlib import Path
from typing import Any

import chromadb
import duckdb
import networkx as nx

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from twin.retrieval.graph import build_graph  # noqa: E402

DEFAULT_DB_PATH = REPO_ROOT / "data" / "knowledge.duckdb"
DEFAULT_CHROMA_PATH = REPO_ROOT / "data" / "chroma"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "data" / "exports" / "relationships"
DEFAULT_VIZ_DATA_DIR = REPO_ROOT / "viz" / "src" / "data"

JSONL_BATCH_SIZE = 1_000
CHROMA_BATCH_SIZE = 250
MAX_EMBEDDING_PART_BYTES = 48 * 1024 * 1024


class ExportValidationError(RuntimeError):
    """Raised when a source or generated export fails consistency checks."""


class _JsonlPartWriter:
    """Write a deterministic JSONL stream in GitHub-compatible file parts."""

    def __init__(self, base_path: Path, max_bytes: int = MAX_EMBEDDING_PART_BYTES) -> None:
        if max_bytes <= 0:
            raise ValueError("JSONL part size must be positive")
        self.base_path = base_path
        self.max_bytes = max_bytes
        self.paths: list[Path] = []
        self._handle: Any = None
        self._bytes = 0

    def __enter__(self) -> _JsonlPartWriter:
        self.base_path.parent.mkdir(parents=True, exist_ok=True)
        self._open_next()
        return self

    def _open_next(self) -> None:
        if self._handle is not None:
            self._handle.close()
        path = self.base_path.parent / (
            f"{self.base_path.name}.part-{len(self.paths) + 1:04d}.jsonl"
        )
        self.paths.append(path)
        self._handle = path.open("w", encoding="utf-8", newline="\n")
        self._bytes = 0

    def write(self, record: Mapping[str, Any]) -> None:
        line = _canonical_json(record) + "\n"
        line_bytes = len(line.encode("utf-8"))
        if line_bytes > self.max_bytes:
            raise ExportValidationError(
                f"One JSONL record exceeds the {self.max_bytes:,}-byte part limit"
            )
        if self._bytes and self._bytes + line_bytes > self.max_bytes:
            self._open_next()
        self._handle.write(line)
        self._bytes += line_bytes

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        if self._handle is not None:
            self._handle.close()
            self._handle = None


def _normalise(value: Any) -> Any:
    """Convert database and numeric values into strict, deterministic JSON values."""
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ExportValidationError(f"Cannot export non-finite float: {value}")
        return value
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, (datetime, date, time)):
        return value.isoformat()
    if isinstance(value, bytes):
        return {"encoding": "base64", "data": base64.b64encode(value).decode("ascii")}
    if isinstance(value, Mapping):
        return {str(key): _normalise(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        items = [_normalise(item) for item in value]
        return sorted(items, key=_canonical_json) if isinstance(value, set) else items
    if hasattr(value, "tolist"):
        return _normalise(value.tolist())
    if hasattr(value, "item"):
        return _normalise(value.item())
    return str(value)


def _canonical_json(value: Any) -> str:
    return json.dumps(
        _normalise(value),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            _normalise(value),
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
        + "\n",
        encoding="utf-8",
    )


def _write_jsonl(path: Path, records: Iterable[Mapping[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(_canonical_json(record))
            handle.write("\n")
            count += 1
    return count


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def _relative_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path.resolve())


def _file_info(path: Path, root: Path) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": _relative_path(path, root),
        "bytes": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
        "sha256": _sha256(path),
    }


def _tree_inventory(directory: Path, root: Path) -> tuple[list[dict[str, Any]], str]:
    files = [_file_info(path, root) for path in sorted(directory.rglob("*")) if path.is_file()]
    digest = hashlib.sha256()
    for item in files:
        digest.update(_canonical_json(item).encode("utf-8"))
        digest.update(b"\n")
    return files, digest.hexdigest()


def _quote_identifier(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def _duckdb_schema(conn: duckdb.DuckDBPyConnection) -> dict[str, Any]:
    tables = sorted(row[0] for row in conn.execute("SHOW TABLES").fetchall())
    constraints_by_table: dict[str, list[dict[str, Any]]] = {table: [] for table in tables}
    for row in conn.execute(
        "SELECT table_name, constraint_type, constraint_text, constraint_column_names, "
        "referenced_table, referenced_column_names "
        "FROM duckdb_constraints() ORDER BY table_name, constraint_index"
    ).fetchall():
        table, kind, text, columns, referenced_table, referenced_columns = row
        if table in constraints_by_table:
            constraints_by_table[table].append(
                {
                    "type": kind,
                    "text": text,
                    "columns": columns or [],
                    "referenced_table": referenced_table,
                    "referenced_columns": referenced_columns or [],
                }
            )

    result: dict[str, Any] = {"tables": {}}
    for table in tables:
        columns = conn.execute(
            "SELECT column_name, data_type, is_nullable, column_default "
            "FROM information_schema.columns "
            "WHERE table_schema = current_schema() AND table_name = ? "
            "ORDER BY ordinal_position",
            [table],
        ).fetchall()
        count = conn.execute(f"SELECT COUNT(*) FROM {_quote_identifier(table)}").fetchone()[0]
        result["tables"][table] = {
            "row_count": count,
            "columns": [
                {
                    "name": name,
                    "type": data_type,
                    "nullable": nullable == "YES",
                    "default": default,
                }
                for name, data_type, nullable, default in columns
            ],
            "constraints": constraints_by_table[table],
        }
    return result


def _schema_yaml(schema: Mapping[str, Any]) -> str:
    """Render the small schema structure as YAML without another dependency."""
    lines = ["version: 1", "tables:"]
    for table, details in schema["tables"].items():
        lines.append(f"  {_canonical_json(table)}:")
        lines.append(f"    row_count: {details['row_count']}")
        lines.append("    columns:")
        for column in details["columns"]:
            lines.extend(
                [
                    f"      - name: {_canonical_json(column['name'])}",
                    f"        type: {_canonical_json(column['type'])}",
                    f"        nullable: {str(column['nullable']).lower()}",
                    f"        default: {_canonical_json(column['default'])}",
                ]
            )
        lines.append("    constraints:")
        if not details["constraints"]:
            lines[-1] = "    constraints: []"
        for constraint in details["constraints"]:
            lines.extend(
                [
                    f"      - type: {_canonical_json(constraint['type'])}",
                    f"        text: {_canonical_json(constraint['text'])}",
                    f"        columns: {_canonical_json(constraint['columns'])}",
                    f"        referenced_table: {_canonical_json(constraint['referenced_table'])}",
                    "        referenced_columns: "
                    f"{_canonical_json(constraint['referenced_columns'])}",
                ]
            )
    return "\n".join(lines) + "\n"


def _stream_query(
    conn: duckdb.DuckDBPyConnection,
    sql: str,
    *,
    params: Sequence[Any] | None = None,
    json_columns: set[str] | None = None,
) -> Iterator[dict[str, Any]]:
    cursor = conn.execute(sql, list(params or []))
    names = [item[0] for item in cursor.description]
    json_columns = json_columns or set()
    while rows := cursor.fetchmany(JSONL_BATCH_SIZE):
        for row in rows:
            record = dict(zip(names, row, strict=True))
            for column in json_columns:
                raw = record.get(column)
                if isinstance(raw, str):
                    try:
                        record[column] = json.loads(raw)
                    except json.JSONDecodeError as exc:
                        raise ExportValidationError(
                            f"Invalid JSON in exported column {column}: {exc}"
                        ) from exc
            yield _normalise(record)


def _table_order(columns: list[dict[str, Any]], constraints: list[dict[str, Any]]) -> list[str]:
    for constraint in constraints:
        if constraint["type"] == "PRIMARY KEY" and constraint["columns"]:
            return list(constraint["columns"])
    names = [column["name"] for column in columns]
    return ["id"] if "id" in names else names


def _export_duckdb_tables(
    conn: duckdb.DuckDBPyConnection,
    schema: dict[str, Any],
    output_root: Path,
) -> dict[str, int]:
    counts: dict[str, int] = {}
    for table, details in schema["tables"].items():
        columns = details["columns"]
        json_columns = {column["name"] for column in columns if column["type"] == "JSON"}
        order = _table_order(columns, details["constraints"])
        order_sql = ", ".join(_quote_identifier(column) for column in order)
        sql = f"SELECT * FROM {_quote_identifier(table)} ORDER BY {order_sql}"
        path = output_root / "duckdb" / "tables" / f"{table}.jsonl"
        count = _write_jsonl(path, _stream_query(conn, sql, json_columns=json_columns))
        expected = details["row_count"]
        if count != expected:
            raise ExportValidationError(f"{table}: exported {count} rows, expected {expected}")
        counts[table] = count
    return counts


def _edge_records(conn: duckdb.DuckDBPyConnection) -> Iterator[dict[str, Any]]:
    sql = """
        SELECT e.id, e.source_id, e.target_id, e.type, e.properties,
               e.weight, e.created_at, e.source_artifact_id, e.confidence,
               sn.type AS source_type, sn.name AS source_name,
               tn.type AS target_type, tn.name AS target_name,
               a.file_name AS artifact_file_name,
               a.file_path AS artifact_file_path,
               a.source_channel AS artifact_source_channel
        FROM edges e
        JOIN nodes sn ON sn.id = e.source_id
        JOIN nodes tn ON tn.id = e.target_id
        LEFT JOIN artifacts a ON a.id = e.source_artifact_id
        ORDER BY e.source_id, e.target_id, e.type, e.id
    """
    for row in _stream_query(conn, sql, json_columns={"properties"}):
        artifact_id = row.pop("source_artifact_id")
        artifact = None
        if row["artifact_file_name"] is not None:
            artifact = {
                "id": artifact_id,
                "file_name": row.pop("artifact_file_name"),
                "file_path": row.pop("artifact_file_path"),
                "source_channel": row.pop("artifact_source_channel"),
            }
        else:
            row.pop("artifact_file_name")
            row.pop("artifact_file_path")
            row.pop("artifact_source_channel")
        yield {
            "id": row["id"],
            "source": {
                "id": row["source_id"],
                "type": row["source_type"],
                "name": row["source_name"],
            },
            "target": {
                "id": row["target_id"],
                "type": row["target_type"],
                "name": row["target_name"],
            },
            "type": row["type"],
            "properties": row["properties"],
            "weight": row["weight"],
            "confidence": row["confidence"],
            "created_at": row["created_at"],
            "source_artifact_id": artifact_id,
            "source_artifact": artifact,
            "source_artifact_missing": artifact_id is not None and artifact is None,
        }


def _projection_specs() -> list[tuple[str, str, set[str]]]:
    return [
        (
            "artifact_classifications.jsonl",
            "SELECT id AS artifact_id, classification FROM artifacts ORDER BY id",
            {"classification"},
        ),
        (
            "person_relationship_labels.jsonl",
            "SELECT id AS person_id, name, "
            "json_extract_string(properties, '$.relationship') AS relationship, "
            "properties FROM nodes WHERE type = 'person' ORDER BY id",
            {"properties"},
        ),
        (
            "edge_artifact_links.jsonl",
            "SELECT e.id AS edge_id, e.source_artifact_id AS artifact_id, "
            "a.id IS NOT NULL AS artifact_exists FROM edges e "
            "LEFT JOIN artifacts a ON a.id = e.source_artifact_id "
            "ORDER BY e.id",
            set(),
        ),
        (
            "chunk_artifact_links.jsonl",
            "SELECT c.id AS chunk_id, c.artifact_id, c.sequence, c.section, "
            "a.id IS NOT NULL AS artifact_exists FROM chunks c "
            "LEFT JOIN artifacts a ON a.id = c.artifact_id ORDER BY c.id",
            set(),
        ),
        (
            "ingestion_artifact_links.jsonl",
            "SELECT l.id AS ingestion_log_id, l.artifact_id, "
            "a.id IS NOT NULL AS artifact_exists FROM ingestion_log l "
            "LEFT JOIN artifacts a ON a.id = l.artifact_id "
            "WHERE l.artifact_id IS NOT NULL ORDER BY l.id",
            set(),
        ),
        (
            "node_source_artifact_links.jsonl",
            "SELECT n.id AS node_id, u.artifact_id, u.ordinality, "
            "a.id IS NOT NULL AS artifact_exists FROM nodes n, "
            "UNNEST(n.source_artifacts) WITH ORDINALITY AS u(artifact_id, ordinality) "
            "LEFT JOIN artifacts a ON a.id = u.artifact_id "
            "ORDER BY n.id, u.ordinality, u.artifact_id",
            set(),
        ),
        (
            "evidence_people.jsonl",
            "SELECT e.id AS evidence_id, e.file_path, e.title, u.person, u.ordinality "
            "FROM evidence_index e, "
            "UNNEST(e.people) WITH ORDINALITY AS u(person, ordinality) "
            "ORDER BY e.id, u.ordinality, u.person",
            set(),
        ),
        (
            "evidence_skills.jsonl",
            "SELECT e.id AS evidence_id, e.file_path, e.title, u.skill, u.ordinality "
            "FROM evidence_index e, "
            "UNNEST(e.skills) WITH ORDINALITY AS u(skill, ordinality) "
            "ORDER BY e.id, u.ordinality, u.skill",
            set(),
        ),
        (
            "evidence_programs.jsonl",
            "SELECT e.id AS evidence_id, e.file_path, e.title, u.program, u.ordinality "
            "FROM evidence_index e, "
            "UNNEST(e.programs) WITH ORDINALITY AS u(program, ordinality) "
            "ORDER BY e.id, u.ordinality, u.program",
            set(),
        ),
    ]


def _export_relationship_projections(
    conn: duckdb.DuckDBPyConnection, output_root: Path
) -> dict[str, int]:
    destination = output_root / "duckdb" / "relationships"
    counts = {
        "edges_enriched.jsonl": _write_jsonl(
            destination / "edges_enriched.jsonl", _edge_records(conn)
        )
    }
    for filename, sql, json_columns in _projection_specs():
        counts[filename] = _write_jsonl(
            destination / filename,
            _stream_query(conn, sql, json_columns=json_columns),
        )
    return counts


def _duckdb_integrity(conn: duckdb.DuckDBPyConnection) -> dict[str, int]:
    queries = {
        "orphan_edge_sources": "SELECT COUNT(*) FROM edges e LEFT JOIN nodes n "
        "ON n.id=e.source_id WHERE n.id IS NULL",
        "orphan_edge_targets": "SELECT COUNT(*) FROM edges e LEFT JOIN nodes n "
        "ON n.id=e.target_id WHERE n.id IS NULL",
        "orphan_chunk_artifacts": "SELECT COUNT(*) FROM chunks c LEFT JOIN artifacts a "
        "ON a.id=c.artifact_id WHERE a.id IS NULL",
        "orphan_edge_artifact_provenance": "SELECT COUNT(*) FROM edges e LEFT JOIN artifacts a "
        "ON a.id=e.source_artifact_id WHERE e.source_artifact_id IS NOT NULL AND a.id IS NULL",
        "orphan_ingestion_artifacts": "SELECT COUNT(*) FROM ingestion_log l LEFT JOIN artifacts a "
        "ON a.id=l.artifact_id WHERE l.artifact_id IS NOT NULL AND a.id IS NULL",
        "self_loops": "SELECT COUNT(*) FROM edges WHERE source_id=target_id",
        "duplicate_ordered_edge_pairs": "SELECT COUNT(*) FROM (SELECT source_id,target_id,"
        "COUNT(*) n FROM edges GROUP BY 1,2 HAVING n>1)",
    }
    result = {name: conn.execute(sql).fetchone()[0] for name, sql in queries.items()}
    if result["orphan_edge_sources"] or result["orphan_edge_targets"]:
        raise ExportValidationError("Edges contain missing node endpoints")
    if result["orphan_chunk_artifacts"]:
        raise ExportValidationError("Chunks contain missing artifact references")
    return result


def _safe_collection_slug(name: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", name).strip("._")
    return slug or "collection"


def _collection_names(client: Any) -> list[str]:
    names = []
    for item in client.list_collections():
        names.append(item if isinstance(item, str) else item.name)
    return sorted(names)


def _all_collection_ids(collection: Any) -> list[str]:
    expected = collection.count()
    ids: list[str] = []
    for offset in range(0, expected, JSONL_BATCH_SIZE):
        page = collection.get(limit=JSONL_BATCH_SIZE, offset=offset, include=[])
        ids.extend(page["ids"])
    if len(ids) != expected or len(set(ids)) != expected:
        raise ExportValidationError(
            f"Chroma collection {collection.name}: expected {expected} unique IDs, got {len(ids)}"
        )
    return sorted(ids)


def _chroma_batch_records(collection: Any, ids: list[str]) -> list[dict[str, Any]]:
    result = collection.get(ids=ids, include=["documents", "metadatas", "embeddings"])
    embeddings = result.get("embeddings")
    documents = result.get("documents") or [None] * len(result["ids"])
    metadatas = result.get("metadatas") or [None] * len(result["ids"])
    records = []
    for index, item_id in enumerate(result["ids"]):
        embedding = None if embeddings is None else _normalise(embeddings[index])
        records.append(
            {
                "id": item_id,
                "document": documents[index],
                "metadata": metadatas[index] or {},
                "embedding": embedding,
            }
        )
    return sorted(records, key=lambda item: item["id"])


def _duckdb_chunks_for_ids(
    conn: duckdb.DuckDBPyConnection, ids: list[str]
) -> dict[str, tuple[str, int, str | None, str]]:
    if not ids:
        return {}
    rows = conn.execute(
        "SELECT id, artifact_id, sequence, section, content FROM chunks "
        "WHERE id IN (SELECT UNNEST(?))",
        [ids],
    ).fetchall()
    return {row[0]: (row[1], row[2], row[3], row[4]) for row in rows}


def _export_chroma(
    chroma_path: Path,
    conn: duckdb.DuckDBPyConnection,
    output_root: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    client = chromadb.PersistentClient(path=str(chroma_path))
    try:
        return _export_chroma_client(client, conn, output_root)
    finally:
        client.close()


def _export_chroma_client(
    client: Any,
    conn: duckdb.DuckDBPyConnection,
    output_root: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    artifact_ids = {row[0] for row in conn.execute("SELECT id FROM artifacts").fetchall()}
    duck_chunk_ids = {row[0] for row in conn.execute("SELECT id FROM chunks").fetchall()}
    inventory: dict[str, Any] = {"collections": {}}
    combined_validation = {
        "duckdb_chunk_ids": len(duck_chunk_ids),
        "chroma_ids": 0,
        "overlap": 0,
        "missing_in_chroma": 0,
        "extra_in_chroma": 0,
        "orphan_artifact_links": 0,
        "document_mismatches": 0,
        "metadata_mismatches": 0,
    }

    used_slugs: set[str] = set()
    relationship_collection_ids: set[str] = set()
    for name in _collection_names(client):
        collection = client.get_collection(name=name)
        start_count = collection.count()
        ids = _all_collection_ids(collection)
        slug = _safe_collection_slug(name)
        if slug in used_slugs:
            slug = f"{slug}_{hashlib.sha256(name.encode()).hexdigest()[:8]}"
        used_slugs.add(slug)

        records_path = output_root / "chromadb" / f"{slug}.jsonl"
        embeddings_base = output_root / "chromadb" / f"{slug}_embeddings"
        links_path = output_root / "chromadb" / f"{slug}_artifact_links.jsonl"
        records_path.parent.mkdir(parents=True, exist_ok=True)
        record_count = embedding_count = link_count = 0
        dimension: int | None = None
        collection_ids: set[str] = set()

        with (
            records_path.open("w", encoding="utf-8", newline="\n") as records_file,
            _JsonlPartWriter(embeddings_base) as embeddings_writer,
            links_path.open("w", encoding="utf-8", newline="\n") as links_file,
        ):
            for offset in range(0, len(ids), CHROMA_BATCH_SIZE):
                requested = ids[offset : offset + CHROMA_BATCH_SIZE]
                batch = _chroma_batch_records(collection, requested)
                duck_rows = _duckdb_chunks_for_ids(conn, [item["id"] for item in batch])
                for item in batch:
                    item_id = item["id"]
                    metadata = _normalise(item["metadata"])
                    embedding = item["embedding"]
                    if embedding is not None:
                        current_dimension = len(embedding)
                        dimension = dimension or current_dimension
                        if dimension != current_dimension:
                            raise ExportValidationError(
                                f"Chroma collection {name} has inconsistent dimensions"
                            )
                    records_file.write(
                        _canonical_json(
                            {"id": item_id, "document": item["document"], "metadata": metadata}
                        )
                        + "\n"
                    )
                    embeddings_writer.write({"id": item_id, "embedding": embedding})
                    artifact_id = (
                        metadata.get("artifact_id") if isinstance(metadata, dict) else None
                    )
                    artifact_exists = (
                        artifact_id in artifact_ids if artifact_id is not None else False
                    )
                    links_file.write(
                        _canonical_json(
                            {
                                "chunk_id": item_id,
                                "artifact_id": artifact_id,
                                "artifact_exists": artifact_exists,
                            }
                        )
                        + "\n"
                    )
                    record_count += 1
                    embedding_count += 1
                    link_count += 1
                    collection_ids.add(item_id)
                    if artifact_id is not None and not artifact_exists:
                        combined_validation["orphan_artifact_links"] += 1

                    if name == "twin_chunks" and item_id in duck_rows:
                        duck_artifact, duck_sequence, duck_section, duck_document = duck_rows[
                            item_id
                        ]
                        if item["document"] != duck_document:
                            combined_validation["document_mismatches"] += 1
                        if (
                            artifact_id != duck_artifact
                            or metadata.get("sequence") != duck_sequence
                            or metadata.get("section") != duck_section
                        ):
                            combined_validation["metadata_mismatches"] += 1

        end_count = collection.count()
        end_ids = set(_all_collection_ids(collection))
        if start_count != end_count or collection_ids != end_ids:
            raise ExportValidationError(f"Chroma collection {name} changed during export")
        if (
            record_count != start_count
            or embedding_count != start_count
            or link_count != start_count
        ):
            raise ExportValidationError(f"Chroma collection {name} export count mismatch")
        if name == "twin_chunks":
            relationship_collection_ids.update(collection_ids)
        inventory["collections"][name] = {
            "slug": slug,
            "count": start_count,
            "dimension": dimension,
            "metadata": _normalise(getattr(collection, "metadata", None) or {}),
            "files": {
                "records": f"chromadb/{slug}.jsonl",
                "embeddings": [
                    path.relative_to(output_root).as_posix() for path in embeddings_writer.paths
                ],
                "artifact_links": f"chromadb/{slug}_artifact_links.jsonl",
            },
        }

    combined_validation.update(
        {
            "chroma_ids": len(relationship_collection_ids),
            "overlap": len(duck_chunk_ids & relationship_collection_ids),
            "missing_in_chroma": len(duck_chunk_ids - relationship_collection_ids),
            "extra_in_chroma": len(relationship_collection_ids - duck_chunk_ids),
        }
    )
    if "twin_chunks" not in inventory["collections"]:
        raise ExportValidationError("Canonical Chroma collection twin_chunks is missing")
    if combined_validation["orphan_artifact_links"]:
        raise ExportValidationError("Chroma contains missing artifact references")
    if combined_validation["extra_in_chroma"]:
        raise ExportValidationError("Chroma contains chunk IDs absent from DuckDB")
    if combined_validation["document_mismatches"] or combined_validation["metadata_mismatches"]:
        raise ExportValidationError("Chroma records differ from matching DuckDB chunks")
    return inventory, combined_validation


def _export_networkx(
    conn: duckdb.DuckDBPyConnection, output_root: Path
) -> tuple[dict[str, Any], dict[str, int]]:
    graph = build_graph(conn)
    node_link = nx.node_link_data(graph, edges="links")
    node_link["nodes"] = sorted(node_link["nodes"], key=lambda item: item["id"])
    node_link["links"] = sorted(
        node_link["links"],
        key=lambda item: (item["source"], item["target"], item.get("type", "")),
    )
    _write_json(output_root / "networkx" / "graph.node-link.json", node_link)

    components = sorted(
        nx.weakly_connected_components(graph),
        key=lambda nodes: (-len(nodes), min(nodes)),
    )
    component_for: dict[str, tuple[str, int]] = {}
    for index, nodes in enumerate(components, start=1):
        component_id = f"weak_component_{index:04d}"
        for node_id in nodes:
            component_for[node_id] = (component_id, len(nodes))

    denominator = max(graph.number_of_nodes() - 1, 1)

    def metric_records() -> Iterator[dict[str, Any]]:
        for node_id in sorted(graph.nodes):
            in_types = Counter(
                data.get("type", "") for _, _, data in graph.in_edges(node_id, data=True)
            )
            out_types = Counter(
                data.get("type", "") for _, _, data in graph.out_edges(node_id, data=True)
            )
            component_id, component_size = component_for[node_id]
            degree = graph.degree(node_id)
            yield {
                "id": node_id,
                "type": graph.nodes[node_id].get("type", ""),
                "name": graph.nodes[node_id].get("name", ""),
                "in_degree": graph.in_degree(node_id),
                "out_degree": graph.out_degree(node_id),
                "degree": degree,
                "degree_centrality": degree / denominator,
                "is_isolate": degree == 0,
                "weak_component_id": component_id,
                "weak_component_size": component_size,
                "in_edge_types": dict(sorted(in_types.items())),
                "out_edge_types": dict(sorted(out_types.items())),
            }

    metric_count = _write_jsonl(output_root / "networkx" / "node_metrics.jsonl", metric_records())
    summary = {
        "graph_class": type(graph).__name__,
        "directed": graph.is_directed(),
        "multigraph": graph.is_multigraph(),
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
        "density": nx.density(graph),
        "self_loops": nx.number_of_selfloops(graph),
        "isolates": nx.number_of_isolates(graph),
        "weak_components": len(components),
        "largest_weak_component": len(components[0]) if components else 0,
        "strong_components": nx.number_strongly_connected_components(graph),
        "runtime_node_attributes": ["name", "type"],
        "runtime_edge_attributes": ["confidence", "type", "weight"],
    }
    _write_json(output_root / "networkx" / "summary.json", summary)
    return summary, {"node_metrics.jsonl": metric_count}


def _json_shape(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"valid_json": False, "error": str(exc)}
    if isinstance(value, dict):
        result: dict[str, Any] = {
            "valid_json": True,
            "top_level_type": "object",
            "top_level_keys": sorted(value),
        }
        if path.name == "graph.json" and isinstance(value.get("force"), dict):
            result["graph_summary"] = {
                "force_nodes": len(value["force"].get("nodes", [])),
                "force_edges": len(value["force"].get("edges", [])),
                "ego_centers": len(value.get("ego_index", {})),
                "radial_items": len(value.get("radial", [])),
            }
        return result
    if isinstance(value, list):
        return {"valid_json": True, "top_level_type": "array", "items": len(value)}
    return {"valid_json": True, "top_level_type": type(value).__name__}


def _derived_viz_inventory(viz_data_dir: Path, repo_root: Path) -> list[dict[str, Any]]:
    if not viz_data_dir.exists():
        return []
    items = []
    for path in sorted(viz_data_dir.glob("*.json")):
        items.append({**_file_info(path, repo_root), **_json_shape(path)})
    return items


def _output_inventory(staging: Path) -> list[dict[str, Any]]:
    items = []
    for path in sorted(staging.rglob("*")):
        if path.is_file() and path.name != "manifest.json":
            item: dict[str, Any] = {
                "path": path.relative_to(staging).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": _sha256(path),
            }
            if path.suffix == ".jsonl":
                with path.open("rb") as handle:
                    item["records"] = sum(1 for _ in handle)
            items.append(item)
    return items


def _consistency_markdown(
    schema: dict[str, Any],
    integrity: dict[str, int],
    chroma: dict[str, Any],
    graph: dict[str, Any],
) -> str:
    table_lines = ["| Table | Rows |", "|---|---:|"]
    table_lines.extend(
        f"| `{name}` | {details['row_count']:,} |" for name, details in schema["tables"].items()
    )
    check_lines = ["| Check | Count |", "|---|---:|"]
    check_lines.extend(f"| `{name}` | {value:,} |" for name, value in sorted(integrity.items()))
    chroma_lines = ["| Check | Count |", "|---|---:|"]
    chroma_lines.extend(f"| `{name}` | {value:,} |" for name, value in chroma.items())
    return (
        "# Relationship export consistency report\n\n"
        "The export preserves the canonical DuckDB tables, Chroma records and embeddings, "
        "and the exact NetworkX runtime graph. Personal data in this directory is private "
        "and must not be committed or published without review.\n\n"
        "## DuckDB tables\n\n"
        + "\n".join(table_lines)
        + "\n\n## Referential and graph checks\n\n"
        + "\n".join(check_lines)
        + "\n\n`orphan_edge_artifact_provenance` and `orphan_ingestion_artifacts` are "
        "soft, non-foreign-key provenance links and are reported rather than hidden.\n\n"
        "## ChromaDB alignment\n\n" + "\n".join(chroma_lines) + "\n\n## Runtime NetworkX graph\n\n"
        f"- Nodes: {graph['nodes']:,}\n"
        f"- Edges: {graph['edges']:,}\n"
        f"- Isolates: {graph['isolates']:,}\n"
        f"- Weak components: {graph['weak_components']:,}\n"
        f"- Largest weak component: {graph['largest_weak_component']:,}\n"
    )


def _readme() -> str:
    return """# Portable relationship export

This directory is generated by `scripts/export_relationships.py` from the canonical
`data/knowledge.duckdb` and `data/chroma` stores.

- `duckdb/tables/` contains every DuckDB table as deterministic JSON Lines.
- `duckdb/relationships/` contains enriched, explicit relationship projections.
- `chromadb/` separates readable documents/metadata from full embedding vectors. Embeddings
  are split into deterministic `.part-NNNN.jsonl` files below 48 MiB for Git hosting.
- `networkx/graph.node-link.json` is the exact graph shape built by production code.
- `networkx/node_metrics.jsonl` adds deterministic degree and component metrics.
- `inventory/` identifies canonical stores and derived visualization JSON.
- `quality/consistency-report.md` records cross-store and referential checks.

The material is private and may contain sensitive personal and professional information. It is
versioned only in the access-controlled private repository by explicit owner decision; do not
deploy, mirror publicly, or share it without another deliberate privacy review.
"""


def _validate_output_target(target: Path, repo_root: Path) -> None:
    resolved = target.resolve()
    protected = {
        Path("/").resolve(),
        repo_root.resolve(),
        (repo_root / "data").resolve(),
        (repo_root / "data" / "exports").resolve(),
    }
    if resolved in protected or resolved == resolved.parent:
        raise ValueError(f"Refusing unsafe export target: {resolved}")


def _atomic_replace_directory(staging: Path, target: Path) -> None:
    backup = target.parent / f".{target.name}.previous-{uuid.uuid4().hex}"
    moved_previous = False
    try:
        if target.exists():
            os.replace(target, backup)
            moved_previous = True
        os.replace(staging, target)
    except Exception:
        if moved_previous and backup.exists() and not target.exists():
            os.replace(backup, target)
        raise
    else:
        if moved_previous:
            shutil.rmtree(backup)


def export_relationships(
    *,
    repo_root: Path = REPO_ROOT,
    db_path: Path | None = None,
    chroma_path: Path | None = None,
    output_dir: Path | None = None,
    viz_data_dir: Path | None = None,
    generated_at_utc: str | None = None,
) -> dict[str, Any]:
    """Export canonical relationships and atomically install the verified snapshot."""
    repo_root = repo_root.resolve()
    db_path = (db_path or repo_root / "data" / "knowledge.duckdb").resolve()
    chroma_path = (chroma_path or repo_root / "data" / "chroma").resolve()
    output_dir = (output_dir or repo_root / "data" / "exports" / "relationships").resolve()
    viz_data_dir = (viz_data_dir or repo_root / "viz" / "src" / "data").resolve()
    _validate_output_target(output_dir, repo_root)
    if not db_path.is_file():
        raise FileNotFoundError(f"DuckDB store not found: {db_path}")
    if not chroma_path.is_dir():
        raise FileNotFoundError(f"ChromaDB store not found: {chroma_path}")

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{output_dir.name}-", dir=output_dir.parent))
    generated_at = generated_at_utc or datetime.now(UTC).isoformat()
    conn: duckdb.DuckDBPyConnection | None = None
    try:
        conn = duckdb.connect(str(db_path), read_only=True)
        schema = _duckdb_schema(conn)
        (staging / "duckdb").mkdir(parents=True, exist_ok=True)
        (staging / "duckdb" / "schema.yml").write_text(
            _schema_yaml(schema), encoding="utf-8", newline="\n"
        )
        table_counts = _export_duckdb_tables(conn, schema, staging)
        relationship_counts = _export_relationship_projections(conn, staging)
        integrity = _duckdb_integrity(conn)

        chroma_inventory, chroma_validation = _export_chroma(chroma_path, conn, staging)
        graph_summary, graph_counts = _export_networkx(conn, staging)

        derived_inventory = _derived_viz_inventory(viz_data_dir, repo_root)
        graph_json = viz_data_dir / "graph.json"
        if graph_json.is_file():
            snapshot = staging / "derived" / "viz_graph.snapshot.json"
            snapshot.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(graph_json, snapshot)

        conn.close()
        conn = None

        duckdb_source = _file_info(db_path, repo_root)
        chroma_files, chroma_tree_hash = _tree_inventory(chroma_path, repo_root)
        source_inventory = {
            "canonical": {
                "duckdb": duckdb_source,
                "chromadb": {
                    "path": _relative_path(chroma_path, repo_root),
                    "tree_sha256": chroma_tree_hash,
                    "files": chroma_files,
                },
            },
            "excluded_noncanonical": ["viz/data/knowledge.duckdb", "viz/data/chroma"],
        }
        _write_json(staging / "inventory" / "source_stores.json", source_inventory)
        _write_json(staging / "inventory" / "derived_viz.json", derived_inventory)
        (staging / "README.md").write_text(_readme(), encoding="utf-8", newline="\n")
        report = _consistency_markdown(schema, integrity, chroma_validation, graph_summary)
        report_path = staging / "quality" / "consistency-report.md"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8", newline="\n")

        outputs = _output_inventory(staging)
        manifest = {
            "schema_version": 2,
            "generated_at_utc": generated_at,
            "generator": "scripts/export_relationships.py",
            "versions": {
                "python": sys.version.split()[0],
                "duckdb": duckdb.__version__,
                "chromadb": chromadb.__version__,
                "networkx": nx.__version__,
            },
            "sources": source_inventory,
            "duckdb": {
                "tables": table_counts,
                "relationship_projections": relationship_counts,
                "integrity": integrity,
            },
            "chromadb": {**chroma_inventory, "validation": chroma_validation},
            "networkx": {"summary": graph_summary, "files": graph_counts},
            "derived_viz": derived_inventory,
            "outputs": outputs,
        }
        _write_json(staging / "manifest.json", manifest)

        for output in outputs:
            path = staging / output["path"]
            if not path.is_file() or _sha256(path) != output["sha256"]:
                raise ExportValidationError(f"Output checksum validation failed: {path}")
        _atomic_replace_directory(staging, output_dir)
        return manifest
    except Exception:
        if conn is not None:
            conn.close()
        if staging.exists():
            shutil.rmtree(staging)
        raise


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB_PATH)
    parser.add_argument("--chroma", type=Path, default=DEFAULT_CHROMA_PATH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--viz-data", type=Path, default=DEFAULT_VIZ_DATA_DIR)
    args = parser.parse_args()
    manifest = export_relationships(
        repo_root=REPO_ROOT,
        db_path=args.db,
        chroma_path=args.chroma,
        output_dir=args.output,
        viz_data_dir=args.viz_data,
    )
    tables = manifest["duckdb"]["tables"]
    chroma_total = sum(item["count"] for item in manifest["chromadb"]["collections"].values())
    graph = manifest["networkx"]["summary"]
    print(f"Exported {sum(tables.values()):,} DuckDB rows")
    print(f"Exported {chroma_total:,} Chroma records and embeddings")
    print(f"Exported NetworkX graph with {graph['nodes']:,} nodes / {graph['edges']:,} edges")
    print(f"Output: {args.output.resolve()}")


if __name__ == "__main__":
    main()
