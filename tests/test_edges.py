"""Tests for graph edge creation."""

from pathlib import Path

import pytest

from twin.db import get_connection, init_schema
from twin.ingestion.classifier import ClassificationResult
from twin.ingestion.edges import create_edges
from twin.ingestion.resolver import ResolutionResult, ResolvedEntity


@pytest.fixture
def db(tmp_path: Path):
    db_path = tmp_path / "test.duckdb"
    init_schema(db_path)
    conn = get_connection(db_path)
    conn.execute(
        "INSERT INTO nodes (id, type, name) VALUES "
        "('proj_1', 'project', 'Chitta'), "
        "('skill_1', 'skill', 'Python'), "
        "('skill_2', 'skill', 'NLP'), "
        "('person_1', 'person', 'Sarah Chen'), "
        "('org_1', 'organization', 'IBM'), "
        "('ach_1', 'achievement', 'IBM Time Management Cert'), "
        "('tr_1', 'time_range', '2008-06-30')"
    )
    conn.execute(
        "INSERT INTO artifacts (id, file_name, file_type, content_hash, source_channel) "
        "VALUES ('art_1', 'email.eml', 'email', 'abc123', 'cli')"
    )
    yield conn
    conn.close()


def _make_resolution(nodes: list[ResolvedEntity]) -> ResolutionResult:
    result = ResolutionResult()
    for n in nodes:
        if n.is_new:
            result.nodes_created.append(n)
        else:
            result.nodes_matched.append(n)
    return result


class TestCreateEdges:
    def test_project_to_skill_edges(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="proj_1", type="project", name="Chitta", is_new=False),
                ResolvedEntity(node_id="skill_1", type="skill", name="Python", is_new=False),
                ResolvedEntity(node_id="skill_2", type="skill", name="NLP", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.9)

        count = create_edges(resolution, classification, "art_1", db)

        edges = db.execute(
            "SELECT source_id, target_id, type FROM edges WHERE type = 'USED_SKILL'"
        ).fetchall()
        assert len(edges) == 2
        assert ("proj_1", "skill_1", "USED_SKILL") in edges
        assert ("proj_1", "skill_2", "USED_SKILL") in edges
        assert count == 2

    def test_person_to_project_edges(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="proj_1", type="project", name="Chitta", is_new=False),
                ResolvedEntity(node_id="person_1", type="person", name="Sarah", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.9)

        create_edges(resolution, classification, "art_1", db)

        edges = db.execute(
            "SELECT source_id, target_id, type FROM edges WHERE type = 'COLLABORATED_WITH'"
        ).fetchall()
        assert len(edges) == 1
        assert edges[0] == ("person_1", "proj_1", "COLLABORATED_WITH")

    def test_person_skill_edge_when_no_projects(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="person_1", type="person", name="Sarah", is_new=False),
                ResolvedEntity(node_id="skill_1", type="skill", name="Python", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.8)

        create_edges(resolution, classification, "art_1", db)

        edges = db.execute("SELECT source_id, target_id, type FROM edges").fetchall()
        assert ("person_1", "skill_1", "USED_SKILL") in edges

    def test_person_skill_edge_skipped_when_projects_exist(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="proj_1", type="project", name="Chitta", is_new=False),
                ResolvedEntity(node_id="person_1", type="person", name="Sarah", is_new=False),
                ResolvedEntity(node_id="skill_1", type="skill", name="Python", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.9)

        create_edges(resolution, classification, "art_1", db)

        edges = db.execute("SELECT source_id, target_id, type FROM edges").fetchall()
        # person->skill should NOT exist when projects are present
        assert ("person_1", "skill_1", "USED_SKILL") not in edges
        # project->skill should exist
        assert ("proj_1", "skill_1", "USED_SKILL") in edges

    def test_no_duplicate_edges(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="proj_1", type="project", name="Chitta", is_new=False),
                ResolvedEntity(node_id="skill_1", type="skill", name="Python", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.9)

        count1 = create_edges(resolution, classification, "art_1", db)
        count2 = create_edges(resolution, classification, "art_1", db)

        total = db.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
        assert count1 == 1
        assert count2 == 0
        assert total == 1

    def test_empty_resolution_creates_no_edges(self, db):
        resolution = _make_resolution([])
        classification = ClassificationResult(confidence=0.5)

        count = create_edges(resolution, classification, "art_1", db)
        assert count == 0

    def test_artifact_id_stored_on_edges(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="proj_1", type="project", name="Chitta", is_new=False),
                ResolvedEntity(node_id="skill_1", type="skill", name="Python", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.9)

        create_edges(resolution, classification, "art_1", db)

        row = db.execute("SELECT source_artifact_id FROM edges LIMIT 1").fetchone()
        assert row[0] == "art_1"

    def test_confidence_stored_on_edges(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="proj_1", type="project", name="Chitta", is_new=False),
                ResolvedEntity(node_id="skill_1", type="skill", name="Python", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.77)

        create_edges(resolution, classification, "art_1", db)

        row = db.execute("SELECT confidence FROM edges LIMIT 1").fetchone()
        assert row[0] == 0.77

    def test_achievement_to_project_recognized_for(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="ach_1", type="achievement", name="Cert", is_new=False),
                ResolvedEntity(node_id="proj_1", type="project", name="Chitta", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.9)

        create_edges(resolution, classification, "art_1", db)

        edges = db.execute(
            "SELECT source_id, target_id, type FROM edges WHERE type = 'RECOGNIZED_FOR'"
        ).fetchall()
        assert ("ach_1", "proj_1", "RECOGNIZED_FOR") in edges

    def test_achievement_to_skill_recognized_for(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="ach_1", type="achievement", name="Cert", is_new=False),
                ResolvedEntity(node_id="skill_1", type="skill", name="Python", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.9)

        create_edges(resolution, classification, "art_1", db)

        edges = db.execute(
            "SELECT source_id, target_id, type FROM edges WHERE type = 'RECOGNIZED_FOR'"
        ).fetchall()
        assert ("ach_1", "skill_1", "RECOGNIZED_FOR") in edges

    def test_achievement_to_org_at_org(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="ach_1", type="achievement", name="Cert", is_new=False),
                ResolvedEntity(node_id="org_1", type="organization", name="IBM", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.9)

        create_edges(resolution, classification, "art_1", db)

        edges = db.execute(
            "SELECT source_id, target_id, type FROM edges WHERE type = 'AT_ORG'"
        ).fetchall()
        assert ("ach_1", "org_1", "AT_ORG") in edges

    def test_achievement_to_time_range_during(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="ach_1", type="achievement", name="Cert", is_new=False),
                ResolvedEntity(node_id="tr_1", type="time_range", name="2008-06-30", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.9)

        create_edges(resolution, classification, "art_1", db)

        edges = db.execute(
            "SELECT source_id, target_id, type FROM edges WHERE type = 'DURING'"
        ).fetchall()
        assert ("ach_1", "tr_1", "DURING") in edges

    def test_project_to_org_at_org(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="proj_1", type="project", name="Chitta", is_new=False),
                ResolvedEntity(node_id="org_1", type="organization", name="IBM", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.85)

        create_edges(resolution, classification, "art_1", db)

        edges = db.execute(
            "SELECT source_id, target_id, type FROM edges WHERE type = 'AT_ORG'"
        ).fetchall()
        assert ("proj_1", "org_1", "AT_ORG") in edges

    def test_project_to_time_range_during(self, db):
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="proj_1", type="project", name="Chitta", is_new=False),
                ResolvedEntity(node_id="tr_1", type="time_range", name="2008-06-30", is_new=False),
            ]
        )
        classification = ClassificationResult(confidence=0.85)

        create_edges(resolution, classification, "art_1", db)

        edges = db.execute(
            "SELECT source_id, target_id, type FROM edges WHERE type = 'DURING'"
        ).fetchall()
        assert ("proj_1", "tr_1", "DURING") in edges

    def test_full_certificate_scenario(self, db):
        """Integration: certificate with achievement, org, skills, and time range."""
        resolution = _make_resolution(
            [
                ResolvedEntity(node_id="ach_1", type="achievement", name="Cert", is_new=True),
                ResolvedEntity(node_id="org_1", type="organization", name="IBM", is_new=False),
                ResolvedEntity(node_id="skill_1", type="skill", name="Python", is_new=False),
                ResolvedEntity(node_id="tr_1", type="time_range", name="2008-06-30", is_new=True),
            ]
        )
        classification = ClassificationResult(confidence=0.95)

        count = create_edges(resolution, classification, "art_1", db)

        edges = db.execute("SELECT source_id, target_id, type FROM edges").fetchall()
        assert ("ach_1", "skill_1", "RECOGNIZED_FOR") in edges
        assert ("ach_1", "org_1", "AT_ORG") in edges
        assert ("ach_1", "tr_1", "DURING") in edges
        assert count == 3
