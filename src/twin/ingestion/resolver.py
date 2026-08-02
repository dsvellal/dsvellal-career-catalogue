"""Entity resolution: match classified entities to existing graph nodes or create new ones."""

import json
import uuid
from dataclasses import dataclass, field

import duckdb

from twin.ingestion.classifier import ClassificationResult


@dataclass
class ResolvedEntity:
    node_id: str
    type: str
    name: str
    is_new: bool
    confidence: float = 1.0


@dataclass
class ResolutionResult:
    nodes_created: list[ResolvedEntity] = field(default_factory=list)
    nodes_matched: list[ResolvedEntity] = field(default_factory=list)

    @property
    def all_nodes(self) -> list[ResolvedEntity]:
        return self.nodes_created + self.nodes_matched


def resolve(
    classification: ClassificationResult, conn: duckdb.DuckDBPyConnection
) -> ResolutionResult:
    """Resolve entities from a classification against existing nodes in the graph."""
    result = ResolutionResult()

    for project_name in classification.projects:
        entity = _resolve_node(conn, "project", project_name, classification.confidence)
        _append_entity(result, entity)

    for skill_name in classification.skills:
        entity = _resolve_node(conn, "skill", skill_name, classification.confidence)
        _append_entity(result, entity)

    for person in classification.people:
        name = person.get("name", "")
        if not name:
            continue
        entity = _resolve_node(conn, "person", name, classification.confidence)
        if entity.is_new:
            _update_properties(conn, entity.node_id, {"relationship": person.get("role", "")})
        _append_entity(result, entity)

    for org in classification.organizations:
        name = org.get("name", "")
        if not name:
            continue
        entity = _resolve_node(conn, "organization", name, classification.confidence)
        if entity.is_new:
            _update_properties(conn, entity.node_id, {"type": org.get("role", "")})
        _append_entity(result, entity)

    _resolve_achievement(classification, conn, result)
    _resolve_time_ranges(classification, conn, result)

    return result


def _resolve_achievement(
    classification: ClassificationResult,
    conn: duckdb.DuckDBPyConnection,
    result: ResolutionResult,
) -> None:
    """Create an achievement node when the document type warrants one."""
    achievement_types = {"certificate", "email_appreciation", "recommendation"}
    if classification.type not in achievement_types:
        return
    if not classification.claims:
        return

    name = _derive_achievement_name(classification)
    entity = _resolve_node(conn, "achievement", name, classification.confidence)
    if entity.is_new:
        props = {"type": _map_achievement_type(classification.type)}
        orgs = classification.organizations
        if orgs:
            props["issuer"] = orgs[0].get("name", "")
        dates = classification.dates
        if dates:
            props["date"] = dates[0].get("date", "")
        _update_properties(conn, entity.node_id, props)
    _append_entity(result, entity)


def _resolve_time_ranges(
    classification: ClassificationResult,
    conn: duckdb.DuckDBPyConnection,
    result: ResolutionResult,
) -> None:
    """Create time_range nodes from extracted dates."""
    for date_entry in classification.dates:
        date_str = date_entry.get("date", "")
        if not date_str:
            continue
        entity = _resolve_node(conn, "time_range", date_str, classification.confidence)
        if entity.is_new:
            _update_properties(
                conn,
                entity.node_id,
                {
                    "start": date_str,
                    "end": date_str,
                    "type": "custom",
                    "label": date_entry.get("context", date_str),
                },
            )
        _append_entity(result, entity)


def _derive_achievement_name(classification: ClassificationResult) -> str:
    """Build a descriptive name for the achievement node."""
    parts = []
    orgs = classification.organizations
    if orgs:
        parts.append(orgs[0].get("name", ""))
    if classification.claims:
        parts.append(classification.claims[0])
    return " - ".join(parts) if parts else "Achievement"


def _map_achievement_type(doc_type: str) -> str:
    return {
        "certificate": "certification",
        "email_appreciation": "recognition",
        "recommendation": "recommendation",
    }.get(doc_type, "recognition")


def _resolve_node(
    conn: duckdb.DuckDBPyConnection, node_type: str, name: str, confidence: float
) -> ResolvedEntity:
    """Find existing node by type+name or create a new one."""
    normalized = _normalize_name(name)

    existing = conn.execute(
        "SELECT id, name FROM nodes WHERE type = ? AND LOWER(name) = ?",
        [node_type, normalized],
    ).fetchone()

    if existing:
        return ResolvedEntity(
            node_id=existing[0],
            type=node_type,
            name=existing[1],
            is_new=False,
            confidence=confidence,
        )

    node_id = _generate_id(node_type, name)
    conn.execute(
        "INSERT INTO nodes (id, type, name, confidence) VALUES (?, ?, ?, ?)",
        [node_id, node_type, name, confidence],
    )
    return ResolvedEntity(
        node_id=node_id,
        type=node_type,
        name=name,
        is_new=True,
        confidence=confidence,
    )


def _update_properties(conn: duckdb.DuckDBPyConnection, node_id: str, props: dict) -> None:
    """Merge properties into an existing node's properties JSON."""
    row = conn.execute("SELECT properties FROM nodes WHERE id = ?", [node_id]).fetchone()
    if not row:
        return
    existing = json.loads(row[0]) if row[0] else {}
    existing.update({k: v for k, v in props.items() if v})
    conn.execute("UPDATE nodes SET properties = ? WHERE id = ?", [json.dumps(existing), node_id])


def _normalize_name(name: str) -> str:
    """Normalize a name for matching: lowercase, strip whitespace."""
    return name.strip().lower()


def _generate_id(node_type: str, name: str) -> str:
    """Generate a deterministic-ish ID from type and name."""
    return f"{node_type}_{uuid.uuid5(uuid.NAMESPACE_DNS, f'{node_type}:{name}')}"


def _append_entity(result: ResolutionResult, entity: ResolvedEntity) -> None:
    if entity.is_new:
        result.nodes_created.append(entity)
    else:
        result.nodes_matched.append(entity)
