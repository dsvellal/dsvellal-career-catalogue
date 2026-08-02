"""Tests for the CLI entry point."""

import tempfile
from pathlib import Path
from unittest.mock import patch

from typer.testing import CliRunner

from twin.cli import app
from twin.db import is_initialized

runner = CliRunner()


def test_help_shows_commands():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "twin" in result.output.lower() or "personal knowledge" in result.output.lower()


def test_status_no_db():
    with tempfile.TemporaryDirectory() as tmp:
        db = str(Path(tmp) / "nope.duckdb")
        result = runner.invoke(app, ["status", "--db", db])
        assert result.exit_code == 0
        assert "No database initialized" in result.output


def test_init_creates_database():
    with tempfile.TemporaryDirectory() as tmp:
        db = str(Path(tmp) / "test.duckdb")
        result = runner.invoke(app, ["init", "--db", db])
        assert result.exit_code == 0
        assert "initialized" in result.output.lower()
        assert is_initialized(Path(db))


def test_init_idempotent():
    with tempfile.TemporaryDirectory() as tmp:
        db = str(Path(tmp) / "test.duckdb")
        runner.invoke(app, ["init", "--db", db])
        result = runner.invoke(app, ["init", "--db", db])
        assert result.exit_code == 0
        assert "already initialized" in result.output.lower()


def test_status_after_init():
    with tempfile.TemporaryDirectory() as tmp:
        db = str(Path(tmp) / "test.duckdb")
        runner.invoke(app, ["init", "--db", db])
        result = runner.invoke(app, ["status", "--db", db])
        assert result.exit_code == 0
        assert "Nodes" in result.output
        assert "0" in result.output


def test_status_shows_node_types():
    with tempfile.TemporaryDirectory() as tmp:
        db_file = Path(tmp) / "test.duckdb"
        db = str(db_file)
        runner.invoke(app, ["init", "--db", db])
        f = Path(tmp) / "note.md"
        f.write_text("# Project Alpha\n\nUsing Python and NLP.")

        def _mock(extraction, api_key):
            from twin.ingestion.classifier import ClassificationResult

            return ClassificationResult(projects=["Alpha"], skills=["python"], confidence=0.9)

        with patch("twin.ingestion.pipeline._classify_safe", _mock):
            runner.invoke(app, ["ingest", str(f), "--db", db])
        result = runner.invoke(app, ["status", "--db", db])
        assert result.exit_code == 0
        assert "project" in result.output
        assert "skill" in result.output


def test_ingest_requires_init():
    with tempfile.TemporaryDirectory() as tmp:
        db = str(Path(tmp) / "nope.duckdb")
        f = Path(tmp) / "note.md"
        f.write_text("hello")
        result = runner.invoke(app, ["ingest", str(f), "--db", db])
        assert result.exit_code == 1
        assert "not initialized" in result.output.lower()


def test_ingest_file_not_found():
    with tempfile.TemporaryDirectory() as tmp:
        db = str(Path(tmp) / "test.duckdb")
        runner.invoke(app, ["init", "--db", db])
        result = runner.invoke(app, ["ingest", "/nope/missing.txt", "--db", db])
        assert result.exit_code == 1


def test_ingest_single_file():
    with tempfile.TemporaryDirectory() as tmp:
        db = str(Path(tmp) / "test.duckdb")
        runner.invoke(app, ["init", "--db", db])
        f = Path(tmp) / "note.md"
        f.write_text("# Hello\n\nSome content here.")
        with patch.dict("os.environ", {}, clear=True):
            result = runner.invoke(app, ["ingest", str(f), "--db", db])
        assert result.exit_code == 0
        assert "note.md" in result.output


def test_ingest_directory():
    with tempfile.TemporaryDirectory() as tmp:
        db = str(Path(tmp) / "test.duckdb")
        runner.invoke(app, ["init", "--db", db])
        docs = Path(tmp) / "docs"
        docs.mkdir()
        (docs / "a.md").write_text("File A")
        (docs / "b.txt").write_text("File B")
        with patch.dict("os.environ", {}, clear=True):
            result = runner.invoke(app, ["ingest", str(docs), "--db", db])
        assert result.exit_code == 0
        assert "a.md" in result.output
        assert "b.txt" in result.output


def test_ingest_dedup():
    with tempfile.TemporaryDirectory() as tmp:
        db = str(Path(tmp) / "test.duckdb")
        runner.invoke(app, ["init", "--db", db])
        f = Path(tmp) / "note.md"
        f.write_text("Same content")
        with patch.dict("os.environ", {}, clear=True):
            runner.invoke(app, ["ingest", str(f), "--db", db])
            result = runner.invoke(app, ["ingest", str(f), "--db", db])
        assert "Duplicate" in result.output
