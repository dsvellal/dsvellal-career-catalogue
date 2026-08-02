"""Tests for DuckDB schema initialization and connection management."""

from pathlib import Path

import pytest

from twin.db import get_connection, init_schema, is_initialized

EXPECTED_TABLES = [
    "anonymization_map",
    "artifacts",
    "chunks",
    "edges",
    "gdrive_sync",
    "ingestion_log",
    "nodes",
    "publications",
    "voice_profile",
]


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "test.duckdb"


def test_is_initialized_returns_false_for_missing_file(db_path: Path):
    assert not is_initialized(db_path)


def test_init_schema_creates_all_tables(db_path: Path):
    init_schema(db_path)
    conn = get_connection(db_path)
    tables = sorted(row[0] for row in conn.execute("SHOW TABLES").fetchall())
    conn.close()
    assert tables == EXPECTED_TABLES


def test_init_schema_is_idempotent(db_path: Path):
    init_schema(db_path)
    init_schema(db_path)
    assert is_initialized(db_path)


def test_is_initialized_returns_true_after_init(db_path: Path):
    init_schema(db_path)
    assert is_initialized(db_path)


def test_get_connection_creates_parent_dirs(tmp_path: Path):
    nested = tmp_path / "a" / "b" / "c" / "test.duckdb"
    conn = get_connection(nested)
    conn.close()
    assert nested.parent.exists()


def test_indexes_created(db_path: Path):
    init_schema(db_path)
    conn = get_connection(db_path)
    indexes = conn.execute("SELECT index_name FROM duckdb_indexes() ORDER BY index_name").fetchall()
    conn.close()
    index_names = [row[0] for row in indexes]
    assert "idx_nodes_type" in index_names
    assert "idx_edges_source" in index_names
    assert "idx_artifacts_hash" in index_names


def test_nodes_table_schema(db_path: Path):
    init_schema(db_path)
    conn = get_connection(db_path)
    conn.execute("INSERT INTO nodes (id, type, name) VALUES ('test-1', 'skill', 'Python')")
    row = conn.execute("SELECT id, type, name, confidence FROM nodes").fetchone()
    conn.close()
    assert row == ("test-1", "skill", "Python", 1.0)
