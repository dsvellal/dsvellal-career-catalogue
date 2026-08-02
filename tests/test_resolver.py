"""Tests for entity resolution logic."""

from pathlib import Path

import pytest

from twin.db import get_connection, init_schema
from twin.ingestion.classifier import ClassificationResult
from twin.ingestion.resolver import _generate_id, _normalize_name, resolve


@pytest.fixture
def db(tmp_path: Path):
    db_path = tmp_path / "test.duckdb"
    init_schema(db_path)
    conn = get_connection(db_path)
    yield conn
    conn.close()


class TestResolve:
    def test_creates_new_nodes_for_projects(self, db):
        classification = ClassificationResult(
            projects=["Chitta", "Twin"],
            confidence=0.9,
        )
        result = resolve(classification, db)
        assert len(result.nodes_created) == 2
        assert all(n.type == "project" for n in result.nodes_created)
        names = {n.name for n in result.nodes_created}
        assert names == {"Chitta", "Twin"}

    def test_creates_new_nodes_for_skills(self, db):
        classification = ClassificationResult(
            skills=["python", "knowledge_graphs"],
            confidence=0.85,
        )
        result = resolve(classification, db)
        assert len(result.nodes_created) == 2
        assert all(n.type == "skill" for n in result.nodes_created)

    def test_creates_new_nodes_for_people(self, db):
        classification = ClassificationResult(
            people=[{"name": "Sarah Chen", "role": "VP Engineering"}],
            confidence=0.92,
        )
        result = resolve(classification, db)
        assert len(result.nodes_created) == 1
        assert result.nodes_created[0].name == "Sarah Chen"
        assert result.nodes_created[0].type == "person"

    def test_matches_existing_node_case_insensitive(self, db):
        db.execute("INSERT INTO nodes (id, type, name) VALUES ('proj_1', 'project', 'Chitta')")
        classification = ClassificationResult(projects=["chitta"], confidence=0.9)
        result = resolve(classification, db)
        assert len(result.nodes_matched) == 1
        assert result.nodes_matched[0].node_id == "proj_1"
        assert result.nodes_matched[0].name == "Chitta"
        assert len(result.nodes_created) == 0

    def test_matches_existing_strips_whitespace(self, db):
        db.execute("INSERT INTO nodes (id, type, name) VALUES ('s_1', 'skill', 'Python')")
        classification = ClassificationResult(skills=["  Python  "], confidence=0.8)
        result = resolve(classification, db)
        assert len(result.nodes_matched) == 1
        assert result.nodes_matched[0].node_id == "s_1"

    def test_mixed_new_and_existing(self, db):
        db.execute("INSERT INTO nodes (id, type, name) VALUES ('proj_1', 'project', 'Chitta')")
        classification = ClassificationResult(
            projects=["Chitta", "NewProject"],
            skills=["rust"],
            confidence=0.88,
        )
        result = resolve(classification, db)
        assert len(result.nodes_matched) == 1
        assert len(result.nodes_created) == 2

    def test_skips_people_without_name(self, db):
        classification = ClassificationResult(
            people=[{"name": "", "role": "manager"}, {"role": "peer"}],
            confidence=0.7,
        )
        result = resolve(classification, db)
        assert len(result.all_nodes) == 0

    def test_person_properties_set_on_creation(self, db):
        classification = ClassificationResult(
            people=[{"name": "Alice", "role": "manager"}],
            confidence=0.9,
        )
        resolve(classification, db)
        import json

        row = db.execute("SELECT properties FROM nodes WHERE name = 'Alice'").fetchone()
        props = json.loads(row[0])
        assert props["relationship"] == "manager"

    def test_all_nodes_property(self, db):
        classification = ClassificationResult(projects=["A"], skills=["B"], confidence=0.9)
        result = resolve(classification, db)
        assert len(result.all_nodes) == 2

    def test_confidence_propagated(self, db):
        classification = ClassificationResult(projects=["X"], confidence=0.77)
        result = resolve(classification, db)
        assert result.nodes_created[0].confidence == 0.77

    def test_creates_organization_nodes(self, db):
        classification = ClassificationResult(
            organizations=[{"name": "IBM", "role": "employer"}],
            confidence=0.9,
        )
        result = resolve(classification, db)
        assert len(result.nodes_created) == 1
        assert result.nodes_created[0].type == "organization"
        assert result.nodes_created[0].name == "IBM"

    def test_organization_properties_set(self, db):
        classification = ClassificationResult(
            organizations=[{"name": "Google", "role": "client"}],
            confidence=0.85,
        )
        resolve(classification, db)
        import json

        row = db.execute("SELECT properties FROM nodes WHERE name = 'Google'").fetchone()
        props = json.loads(row[0])
        assert props["type"] == "client"

    def test_skips_organizations_without_name(self, db):
        classification = ClassificationResult(
            organizations=[{"name": "", "role": "employer"}, {"role": "issuer"}],
            confidence=0.8,
        )
        result = resolve(classification, db)
        assert len(result.all_nodes) == 0

    def test_matches_existing_organization(self, db):
        db.execute("INSERT INTO nodes (id, type, name) VALUES ('org_1', 'organization', 'IBM')")
        classification = ClassificationResult(
            organizations=[{"name": "ibm", "role": "employer"}],
            confidence=0.9,
        )
        result = resolve(classification, db)
        assert len(result.nodes_matched) == 1
        assert result.nodes_matched[0].node_id == "org_1"


class TestAchievementResolution:
    def test_creates_achievement_for_certificate(self, db):
        classification = ClassificationResult(
            type="certificate",
            organizations=[{"name": "IBM", "role": "issuer"}],
            claims=["Completed time management training"],
            dates=[{"date": "2008-06-30", "context": "completion date"}],
            confidence=0.95,
        )
        result = resolve(classification, db)
        achievements = [n for n in result.all_nodes if n.type == "achievement"]
        assert len(achievements) == 1
        assert "IBM" in achievements[0].name

    def test_creates_achievement_for_appreciation(self, db):
        classification = ClassificationResult(
            type="email_appreciation",
            claims=["Outstanding demo to leadership"],
            confidence=0.9,
        )
        result = resolve(classification, db)
        achievements = [n for n in result.all_nodes if n.type == "achievement"]
        assert len(achievements) == 1

    def test_no_achievement_for_project_doc(self, db):
        classification = ClassificationResult(
            type="project_doc",
            claims=["Built a system"],
            confidence=0.9,
        )
        result = resolve(classification, db)
        achievements = [n for n in result.all_nodes if n.type == "achievement"]
        assert len(achievements) == 0

    def test_no_achievement_without_claims(self, db):
        classification = ClassificationResult(
            type="certificate",
            claims=[],
            confidence=0.9,
        )
        result = resolve(classification, db)
        achievements = [n for n in result.all_nodes if n.type == "achievement"]
        assert len(achievements) == 0

    def test_achievement_properties_include_issuer_and_date(self, db):
        classification = ClassificationResult(
            type="certificate",
            organizations=[{"name": "IBM", "role": "issuer"}],
            claims=["Time management certification"],
            dates=[{"date": "2008-06-30", "context": "completion"}],
            confidence=0.95,
        )
        resolve(classification, db)
        import json

        row = db.execute("SELECT properties FROM nodes WHERE type = 'achievement'").fetchone()
        props = json.loads(row[0])
        assert props["type"] == "certification"
        assert props["issuer"] == "IBM"
        assert props["date"] == "2008-06-30"


class TestTimeRangeResolution:
    def test_creates_time_range_nodes(self, db):
        classification = ClassificationResult(
            dates=[{"date": "2008-06-30", "context": "completion date"}],
            confidence=0.9,
        )
        result = resolve(classification, db)
        time_ranges = [n for n in result.all_nodes if n.type == "time_range"]
        assert len(time_ranges) == 1
        assert time_ranges[0].name == "2008-06-30"

    def test_time_range_properties(self, db):
        classification = ClassificationResult(
            dates=[{"date": "2024-01-15", "context": "project start"}],
            confidence=0.85,
        )
        resolve(classification, db)
        import json

        row = db.execute("SELECT properties FROM nodes WHERE type = 'time_range'").fetchone()
        props = json.loads(row[0])
        assert props["start"] == "2024-01-15"
        assert props["end"] == "2024-01-15"
        assert props["type"] == "custom"
        assert props["label"] == "project start"

    def test_skips_empty_dates(self, db):
        classification = ClassificationResult(
            dates=[{"date": "", "context": "unknown"}],
            confidence=0.9,
        )
        result = resolve(classification, db)
        time_ranges = [n for n in result.all_nodes if n.type == "time_range"]
        assert len(time_ranges) == 0

    def test_matches_existing_time_range(self, db):
        db.execute("INSERT INTO nodes (id, type, name) VALUES ('tr_1', 'time_range', '2008-06-30')")
        classification = ClassificationResult(
            dates=[{"date": "2008-06-30", "context": "cert date"}],
            confidence=0.9,
        )
        result = resolve(classification, db)
        time_ranges = [n for n in result.all_nodes if n.type == "time_range"]
        assert len(time_ranges) == 1
        assert time_ranges[0].node_id == "tr_1"
        assert not time_ranges[0].is_new


class TestHelpers:
    def test_normalize_name(self):
        assert _normalize_name("  Python  ") == "python"
        assert _normalize_name("UPPER") == "upper"

    def test_generate_id_deterministic(self):
        id1 = _generate_id("project", "Chitta")
        id2 = _generate_id("project", "Chitta")
        assert id1 == id2
        assert id1.startswith("project_")

    def test_generate_id_unique_across_types(self):
        id1 = _generate_id("project", "Python")
        id2 = _generate_id("skill", "Python")
        assert id1 != id2
