"""Graph edge creation from resolved entities and classification data."""

import uuid

import duckdb

from twin.ingestion.classifier import ClassificationResult
from twin.ingestion.resolver import ResolutionResult


def create_edges(
    resolution: ResolutionResult,
    classification: ClassificationResult,
    artifact_id: str,
    conn: duckdb.DuckDBPyConnection,
) -> int:
    """Create edges between resolved entities. All edges are node-to-node.

    Artifact provenance is tracked via source_artifact_id on each edge.
    Returns the number of edges created.
    """
    created = 0

    all_nodes = resolution.all_nodes
    projects = [n for n in all_nodes if n.type == "project"]
    skills = [n for n in all_nodes if n.type == "skill"]
    people = [n for n in all_nodes if n.type == "person"]
    organizations = [n for n in all_nodes if n.type == "organization"]
    achievements = [n for n in all_nodes if n.type == "achievement"]
    time_ranges = [n for n in all_nodes if n.type == "time_range"]

    for project in projects:
        for skill in skills:
            created += _create_edge(
                conn,
                project.node_id,
                skill.node_id,
                "USED_SKILL",
                artifact_id,
                classification.confidence,
            )

    for person in people:
        for project in projects:
            created += _create_edge(
                conn,
                person.node_id,
                project.node_id,
                "COLLABORATED_WITH",
                artifact_id,
                classification.confidence,
            )

    for person in people:
        for skill in skills:
            if not projects:
                created += _create_edge(
                    conn,
                    person.node_id,
                    skill.node_id,
                    "USED_SKILL",
                    artifact_id,
                    classification.confidence,
                )

    for achievement in achievements:
        for project in projects:
            created += _create_edge(
                conn,
                achievement.node_id,
                project.node_id,
                "RECOGNIZED_FOR",
                artifact_id,
                classification.confidence,
            )
        for skill in skills:
            created += _create_edge(
                conn,
                achievement.node_id,
                skill.node_id,
                "RECOGNIZED_FOR",
                artifact_id,
                classification.confidence,
            )
        for org in organizations:
            created += _create_edge(
                conn,
                achievement.node_id,
                org.node_id,
                "AT_ORG",
                artifact_id,
                classification.confidence,
            )
        for tr in time_ranges:
            created += _create_edge(
                conn,
                achievement.node_id,
                tr.node_id,
                "DURING",
                artifact_id,
                classification.confidence,
            )

    for project in projects:
        for org in organizations:
            created += _create_edge(
                conn,
                project.node_id,
                org.node_id,
                "AT_ORG",
                artifact_id,
                classification.confidence,
            )

    for project in projects:
        for tr in time_ranges:
            created += _create_edge(
                conn,
                project.node_id,
                tr.node_id,
                "DURING",
                artifact_id,
                classification.confidence,
            )

    return created


def _create_edge(
    conn: duckdb.DuckDBPyConnection,
    source_id: str,
    target_id: str,
    edge_type: str,
    artifact_id: str,
    confidence: float,
    properties: dict | None = None,
) -> int:
    """Insert an edge if it doesn't already exist. Returns 1 if created, 0 if duplicate."""
    import json

    existing = conn.execute(
        "SELECT id FROM edges WHERE source_id = ? AND target_id = ? AND type = ?",
        [source_id, target_id, edge_type],
    ).fetchone()

    if existing:
        return 0

    edge_id = f"edge_{uuid.uuid4().hex[:12]}"
    props_json = json.dumps(properties) if properties else "{}"

    conn.execute(
        "INSERT INTO edges (id, source_id, target_id, type, source_artifact_id, "
        "confidence, properties) VALUES (?, ?, ?, ?, ?, ?, ?)",
        [edge_id, source_id, target_id, edge_type, artifact_id, confidence, props_json],
    )
    return 1
