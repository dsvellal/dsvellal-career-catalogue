"""Tests for the portable, deterministic relationship export."""

from __future__ import annotations

import gc
import hashlib
import json
from pathlib import Path

import chromadb
import pytest

from scripts.export_relationships import (
    ExportValidationError,
    _JsonlPartWriter,
    export_relationships,
)
from twin.db import get_connection, init_schema


def _jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def _jsonl_parts(root: Path, paths: list[str]) -> list[dict]:
    return [record for path in paths for record in _jsonl(root / path)]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture
def export_fixture(tmp_path: Path) -> dict[str, Path]:
    repo = tmp_path / "repo"
    db_path = repo / "data" / "knowledge.duckdb"
    chroma_path = repo / "data" / "chroma"
    viz_data = repo / "viz" / "src" / "data"
    output = repo / "data" / "exports" / "relationships"
    viz_data.mkdir(parents=True)

    init_schema(db_path)
    conn = get_connection(db_path)
    conn.execute(
        "INSERT INTO artifacts "
        "(id,file_path,file_name,file_type,content_hash,source_channel,metadata,"
        "classification,raw_text,chunk_count) VALUES "
        "('a1','evidence/a.md','a.md','md','hash-a','test',"
        '\'{"nested":{"b":2},"z":1}\','
        '\'{"type":"project_doc","skills":["Python"]}\','
        "'Unicode: नमस्ते\nsecond line',2)"
    )
    conn.execute(
        "INSERT INTO nodes (id,type,name,properties) VALUES "
        "('p1','project','Project One','{\"employer\":\"Example\"}'),"
        "('per1','person','Person One','{\"relationship\":\"mentor\"}'),"
        "('s1','skill','Python','{\"category\":\"technical\"}'),"
        "('s2','skill','Isolated','{}')"
    )
    conn.execute(
        "INSERT INTO edges "
        "(id,source_id,target_id,type,source_artifact_id,weight,confidence) VALUES "
        "('e2','per1','p1','COLLABORATED_WITH','a1',1.0,0.8),"
        "('e1','p1','s1','USED_SKILL','a1',1.0,0.9)"
    )
    conn.execute(
        "INSERT INTO chunks (id,artifact_id,sequence,content,section,metadata) VALUES "
        "('c2','a1',2,'Second chunk','body','{\"source\":\"fixture\"}'),"
        "('c1','a1',1,'First chunk','intro','{\"source\":\"fixture\"}')"
    )
    conn.execute(
        "INSERT INTO ingestion_log (id,action,artifact_id,details,channel) VALUES "
        "('log1','ingest','a1','{\"ok\":true}','test')"
    )
    conn.execute(
        "INSERT INTO evidence_index "
        "(id,file_path,file_name,title,year,people,skills,programs,quotes) VALUES "
        "('ev1','evidence/a.md','a.md','Evidence A',2026,"
        "['Person One'],['Python'],['Program One'],['Strong work'])"
    )
    conn.close()

    client = chromadb.PersistentClient(path=str(chroma_path))
    collection = client.create_collection(
        "twin_chunks", metadata={"hnsw:space": "cosine"}, embedding_function=None
    )
    collection.add(
        ids=["c2", "c1"],
        embeddings=[[0.3, 0.4], [0.1, 0.2]],
        documents=["Second chunk", "First chunk"],
        metadatas=[
            {"artifact_id": "a1", "sequence": 2, "section": "body"},
            {"artifact_id": "a1", "sequence": 1, "section": "intro"},
        ],
    )
    del collection
    client.close()
    gc.collect()

    (viz_data / "graph.json").write_text(
        json.dumps(
            {
                "force": {"nodes": [{"id": "p1"}], "edges": []},
                "ego_index": {},
                "radial": [],
            }
        ),
        encoding="utf-8",
    )
    (viz_data / "timeline.json").write_text('[{"year":2026}]\n', encoding="utf-8")
    return {
        "repo": repo,
        "db": db_path,
        "chroma": chroma_path,
        "viz": viz_data,
        "output": output,
    }


def _run_export(paths: dict[str, Path]) -> dict:
    return export_relationships(
        repo_root=paths["repo"],
        db_path=paths["db"],
        chroma_path=paths["chroma"],
        output_dir=paths["output"],
        viz_data_dir=paths["viz"],
        generated_at_utc="2026-08-06T12:00:00+00:00",
    )


def test_exports_all_stores_with_parsed_json_and_stable_order(export_fixture):
    output = export_fixture["output"]
    output.mkdir(parents=True)
    (output / "old-snapshot.txt").write_text("old", encoding="utf-8")

    manifest = _run_export(export_fixture)

    assert not (output / "old-snapshot.txt").exists()
    assert manifest["duckdb"]["tables"]["artifacts"] == 1
    assert manifest["duckdb"]["tables"]["nodes"] == 4
    assert manifest["duckdb"]["tables"]["edges"] == 2
    assert manifest["duckdb"]["tables"]["chunks"] == 2

    artifact = _jsonl(output / "duckdb" / "tables" / "artifacts.jsonl")[0]
    assert artifact["metadata"] == {"nested": {"b": 2}, "z": 1}
    assert artifact["classification"]["skills"] == ["Python"]
    assert artifact["raw_text"] == "Unicode: नमस्ते\nsecond line"

    edges = _jsonl(output / "duckdb" / "tables" / "edges.jsonl")
    assert [edge["id"] for edge in edges] == ["e1", "e2"]
    enriched = _jsonl(output / "duckdb" / "relationships" / "edges_enriched.jsonl")
    assert len(enriched) == 2
    assert enriched[0]["source"]["name"] == "Project One"
    assert enriched[0]["source_artifact"]["id"] == "a1"

    people = _jsonl(output / "duckdb" / "relationships" / "person_relationship_labels.jsonl")
    assert people == [
        {
            "name": "Person One",
            "person_id": "per1",
            "properties": {"relationship": "mentor"},
            "relationship": "mentor",
        }
    ]
    assert len(_jsonl(output / "duckdb" / "relationships" / "evidence_people.jsonl")) == 1

    chroma_records = _jsonl(output / "chromadb" / "twin_chunks.jsonl")
    assert [item["id"] for item in chroma_records] == ["c1", "c2"]
    assert [item["document"] for item in chroma_records] == ["First chunk", "Second chunk"]
    embedding_paths = manifest["chromadb"]["collections"]["twin_chunks"]["files"]["embeddings"]
    assert embedding_paths == ["chromadb/twin_chunks_embeddings.part-0001.jsonl"]
    embeddings = _jsonl_parts(output, embedding_paths)
    assert [item["id"] for item in embeddings] == ["c1", "c2"]
    assert embeddings[0]["embedding"] == pytest.approx([0.1, 0.2])
    assert embeddings[1]["embedding"] == pytest.approx([0.3, 0.4])

    graph = json.loads((output / "networkx" / "graph.node-link.json").read_text(encoding="utf-8"))
    assert [node["id"] for node in graph["nodes"]] == ["p1", "per1", "s1", "s2"]
    assert len(graph["links"]) == 2
    metrics = _jsonl(output / "networkx" / "node_metrics.jsonl")
    isolated = next(item for item in metrics if item["id"] == "s2")
    assert isolated["is_isolate"] is True
    assert isolated["degree"] == 0

    source_inventory = json.loads(
        (output / "inventory" / "source_stores.json").read_text(encoding="utf-8")
    )
    assert source_inventory["excluded_noncanonical"] == [
        "viz/data/knowledge.duckdb",
        "viz/data/chroma",
    ]
    assert (output / "derived" / "viz_graph.snapshot.json").exists()

    disk_manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    assert disk_manifest["schema_version"] == 2
    assert disk_manifest["generated_at_utc"] == "2026-08-06T12:00:00+00:00"
    for item in disk_manifest["outputs"]:
        exported = output / item["path"]
        assert exported.stat().st_size == item["bytes"]
        assert _sha256(exported) == item["sha256"]


def test_payload_exports_are_deterministic(export_fixture):
    manifest = _run_export(export_fixture)
    output = export_fixture["output"]
    payloads = [
        "duckdb/tables/artifacts.jsonl",
        "duckdb/tables/edges.jsonl",
        "duckdb/relationships/edges_enriched.jsonl",
        "chromadb/twin_chunks.jsonl",
        "networkx/graph.node-link.json",
        "networkx/node_metrics.jsonl",
    ]
    payloads.extend(manifest["chromadb"]["collections"]["twin_chunks"]["files"]["embeddings"])
    first = {name: (output / name).read_bytes() for name in payloads}

    _run_export(export_fixture)

    assert {name: (output / name).read_bytes() for name in payloads} == first
    assert not list(output.parent.glob(".relationships-*"))
    assert not list(output.parent.glob(".relationships.previous-*"))


def test_embedding_writer_splits_without_losing_records(tmp_path: Path):
    base_path = tmp_path / "twin_chunks_embeddings"
    records = [{"id": f"c{index}", "embedding": [0.1, 0.2, 0.3, 0.4]} for index in range(6)]

    with _JsonlPartWriter(base_path, max_bytes=80) as writer:
        for record in records:
            writer.write(record)

    assert len(writer.paths) > 1
    assert all(path.stat().st_size <= 80 for path in writer.paths)
    exported = [item for path in writer.paths for item in _jsonl(path)]
    assert exported == records


def test_failed_validation_preserves_previous_snapshot(export_fixture):
    output = export_fixture["output"]
    output.mkdir(parents=True)
    sentinel = output / "previous.txt"
    sentinel.write_text("keep me", encoding="utf-8")

    client = chromadb.PersistentClient(path=str(export_fixture["chroma"]))
    collection = client.get_collection("twin_chunks", embedding_function=None)
    collection.add(
        ids=["orphan"],
        embeddings=[[0.8, 0.9]],
        documents=["Orphan chunk"],
        metadatas=[{"artifact_id": "missing", "sequence": 1, "section": "body"}],
    )
    del collection
    client.close()
    gc.collect()

    with pytest.raises(ExportValidationError, match="missing artifact references"):
        _run_export(export_fixture)

    assert sentinel.read_text(encoding="utf-8") == "keep me"
    assert not list(output.parent.glob(".relationships-*"))


def test_missing_sources_fail_without_creating_them(tmp_path: Path):
    repo = tmp_path / "repo"
    chroma = repo / "data" / "chroma"
    output = repo / "data" / "exports" / "relationships"
    chroma.mkdir(parents=True)

    with pytest.raises(FileNotFoundError, match="DuckDB store not found"):
        export_relationships(
            repo_root=repo,
            db_path=repo / "data" / "missing.duckdb",
            chroma_path=chroma,
            output_dir=output,
        )

    assert not (repo / "data" / "missing.duckdb").exists()
    assert not output.exists()
