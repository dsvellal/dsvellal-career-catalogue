"""Tests for the end-to-end ingestion pipeline."""

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from twin.db import get_connection, init_schema
from twin.ingestion.pipeline import ingest_file, ingest_pre_classified


@pytest.fixture
def db(tmp_path: Path):
    db_path = tmp_path / "test.duckdb"
    init_schema(db_path)
    conn = get_connection(db_path)
    yield conn
    conn.close()


@pytest.fixture
def sample_md(tmp_path: Path) -> Path:
    f = tmp_path / "notes.md"
    f.write_text("# Project Chitta\n\nBuilt a knowledge graph with Python and NLP.")
    return f


def _mock_classify(text, file_type, api_key=None):
    from twin.ingestion.classifier import ClassificationResult

    return ClassificationResult(
        type="project_doc",
        projects=["Chitta"],
        skills=["python", "nlp"],
        people=[{"name": "Alice", "role": "collaborator"}],
        organizations=[],
        claims=["Built a knowledge graph"],
        confidence=0.88,
    )


class TestIngestFile:
    def test_processes_file_successfully(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            result = ingest_file(sample_md, db, api_key="fake")

        assert result.status == "processed"
        assert result.file_name == "notes.md"
        assert result.file_type == "md"
        assert result.nodes_created == 4  # Chitta, python, nlp, Alice
        assert result.edges_created > 0

    def test_stores_artifact_in_db(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            result = ingest_file(sample_md, db, api_key="fake")

        row = db.execute(
            "SELECT file_name, file_type, status, source_channel FROM artifacts WHERE id = ?",
            [result.artifact_id],
        ).fetchone()
        assert row == ("notes.md", "md", "processed", "cli")

    def test_stores_raw_text(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            result = ingest_file(sample_md, db, api_key="fake")

        row = db.execute(
            "SELECT raw_text FROM artifacts WHERE id = ?", [result.artifact_id]
        ).fetchone()
        assert "knowledge graph" in row[0]

    def test_stores_classification_json(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            result = ingest_file(sample_md, db, api_key="fake")

        row = db.execute(
            "SELECT classification FROM artifacts WHERE id = ?", [result.artifact_id]
        ).fetchone()
        cls = json.loads(row[0])
        assert cls["type"] == "project_doc"
        assert "Chitta" in cls["projects"]

    def test_dedup_skips_same_content(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            r1 = ingest_file(sample_md, db, api_key="fake")
            r2 = ingest_file(sample_md, db, api_key="fake")

        assert r1.status == "processed"
        assert r2.status == "skipped"
        assert r2.skipped_reason == "Duplicate content"

    def test_file_not_found(self, db, tmp_path):
        result = ingest_file(tmp_path / "nope.txt", db)
        assert result.status == "failed"
        assert "not found" in result.skipped_reason.lower()

    def test_works_without_api_key(self, db, sample_md):
        with patch.dict("os.environ", {}, clear=True):
            result = ingest_file(sample_md, db, api_key=None)

        assert result.status == "processed"
        # Local classifier now extracts entities even without API key
        assert result.nodes_created >= 0

    def test_logs_ingestion(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            ingest_file(sample_md, db, api_key="fake")

        row = db.execute("SELECT action, channel FROM ingestion_log").fetchone()
        assert row == ("ingest", "cli")

    def test_audit_log_details(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            result = ingest_file(sample_md, db, api_key="fake")

        row = db.execute("SELECT artifact_id, details FROM ingestion_log").fetchone()
        assert row[0] == result.artifact_id
        details = json.loads(row[1])
        assert details["file"] == "notes.md"
        assert details["nodes_created"] == 4
        assert details["edges_created"] > 0

    def test_audit_log_timestamp_exists(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            ingest_file(sample_md, db, api_key="fake")

        row = db.execute("SELECT timestamp FROM ingestion_log").fetchone()
        assert row[0] is not None

    def test_no_log_on_skip(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            ingest_file(sample_md, db, api_key="fake")
            ingest_file(sample_md, db, api_key="fake")

        count = db.execute("SELECT COUNT(*) FROM ingestion_log").fetchone()[0]
        assert count == 1  # Only the first ingest is logged

    def test_channel_passed_through(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            ingest_file(sample_md, db, channel="gdrive", api_key="fake")

        row = db.execute("SELECT channel FROM ingestion_log").fetchone()
        assert row[0] == "gdrive"

    def test_context_stored_in_metadata(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            result = ingest_file(sample_md, db, context="VP feedback email", api_key="fake")

        row = db.execute(
            "SELECT metadata FROM artifacts WHERE id = ?", [result.artifact_id]
        ).fetchone()
        meta = json.loads(row[0])
        assert meta["user_context"] == "VP feedback email"

    def test_modified_file_ingests_as_new(self, db, tmp_path):
        f = tmp_path / "evolving.md"
        f.write_text("Version 1")
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            r1 = ingest_file(f, db, api_key="fake")

        f.write_text("Version 2 — completely different content")
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            r2 = ingest_file(f, db, api_key="fake")

        assert r1.status == "processed"
        assert r2.status == "processed"
        assert r1.artifact_id != r2.artifact_id

    def test_dedup_returns_existing_artifact_id(self, db, sample_md):
        with patch("twin.ingestion.pipeline.classify", _mock_classify):
            r1 = ingest_file(sample_md, db, api_key="fake")
            r2 = ingest_file(sample_md, db, api_key="fake")

        assert r2.artifact_id == r1.artifact_id


class TestIngestPreClassified:
    def test_creates_nodes_and_edges(self, db):
        classification_data = {
            "type": "certificate",
            "dates": [{"date": "2008-06-01", "context": "award date"}],
            "projects": ["Visual Composition Editor"],
            "skills": ["leadership", "service_composition"],
            "people": [],
            "organizations": [{"name": "IBM", "role": "employer"}],
            "claims": ["Received IBM Bravo Award"],
            "confidence": 0.96,
        }
        result = ingest_pre_classified(
            classification_data=classification_data,
            conn=db,
            file_name="bravo-award.jpg",
            file_type="image",
            raw_text="IBM Bravo Award for leadership",
            media_url="https://example.com/bravo.jpg",
            context="IBM Bravo Award, June 2008",
        )
        assert result.status == "processed"
        assert result.nodes_created > 0
        assert result.edges_created > 0

    def test_stores_artifact_with_media_url(self, db):
        classification_data = {
            "type": "certificate",
            "dates": [],
            "projects": [],
            "skills": ["python"],
            "people": [],
            "organizations": [],
            "claims": ["Got a cert"],
            "confidence": 0.9,
        }
        result = ingest_pre_classified(
            classification_data=classification_data,
            conn=db,
            file_name="cert.jpg",
            media_url="https://photos.google.com/cert.jpg",
        )
        row = db.execute(
            "SELECT media_url, classification FROM artifacts WHERE id = ?",
            [result.artifact_id],
        ).fetchone()
        assert row[0] == "https://photos.google.com/cert.jpg"
        cls = json.loads(row[1])
        assert cls["type"] == "certificate"

    def test_dedup_on_same_content(self, db):
        classification_data = {"type": "other", "confidence": 0.5}
        r1 = ingest_pre_classified(
            classification_data=classification_data,
            conn=db,
            file_name="same.jpg",
            raw_text="identical content",
        )
        r2 = ingest_pre_classified(
            classification_data=classification_data,
            conn=db,
            file_name="same.jpg",
            raw_text="identical content",
        )
        assert r1.status == "processed"
        assert r2.status == "skipped"

    def test_logs_pre_classified_source(self, db):
        classification_data = {
            "type": "certificate",
            "claims": ["Test"],
            "confidence": 0.9,
        }
        ingest_pre_classified(
            classification_data=classification_data,
            conn=db,
            file_name="test.jpg",
            media_url="https://example.com/x.jpg",
        )
        row = db.execute("SELECT details FROM ingestion_log").fetchone()
        details = json.loads(row[0])
        assert details["source"] == "pre_classified"

    def test_creates_achievement_for_certificate(self, db):
        classification_data = {
            "type": "certificate",
            "dates": [{"date": "2008-06-01", "context": "award date"}],
            "projects": [],
            "skills": ["leadership"],
            "people": [],
            "organizations": [{"name": "IBM", "role": "employer"}],
            "claims": ["Received IBM Bravo Award for leadership"],
            "confidence": 0.96,
        }
        result = ingest_pre_classified(
            classification_data=classification_data,
            conn=db,
            file_name="bravo.jpg",
            media_url="https://example.com/bravo.jpg",
        )
        achievements = db.execute("SELECT name FROM nodes WHERE type = 'achievement'").fetchall()
        assert len(achievements) >= 1
        assert result.nodes_created >= 3  # org + skill + achievement + time_range
