"""Tests for full-text search."""

from pathlib import Path

import pytest

from twin.db import get_connection, init_schema
from twin.retrieval.fts import _extract_snippet, init_fts, search_fts


@pytest.fixture
def db(tmp_path: Path):
    db_path = tmp_path / "test.duckdb"
    init_schema(db_path)
    conn = get_connection(db_path)
    conn.execute(
        "INSERT INTO artifacts (id, file_name, file_type, content_hash, source_channel, raw_text) "
        "VALUES "
        "('art_1', 'resume.md', 'md', 'h1', 'cli', "
        "'I built a knowledge graph using Python and NetworkX for compliance'), "
        "('art_2', 'email.eml', 'email', 'h2', 'cli', "
        "'Great work on the demo. The knowledge system is impressive'), "
        "('art_3', 'notes.txt', 'txt', 'h3', 'cli', "
        "'Meeting notes about cloud deployment and kubernetes')"
    )
    init_fts(conn)
    yield conn
    conn.close()


class TestSearchFts:
    def test_finds_matching_documents(self, db):
        results = search_fts("knowledge graph", db)
        assert len(results) >= 1
        ids = [r["id"] for r in results]
        assert "art_1" in ids

    def test_returns_score(self, db):
        results = search_fts("knowledge", db)
        assert all("score" in r for r in results)
        assert results[0]["score"] > 0

    def test_returns_snippet(self, db):
        results = search_fts("knowledge graph", db)
        assert any("knowledge" in r["snippet"].lower() for r in results)

    def test_empty_query_returns_empty(self, db):
        assert search_fts("", db) == []
        assert search_fts("   ", db) == []

    def test_no_match_returns_empty(self, db):
        results = search_fts("xyznonexistent", db)
        assert results == []

    def test_respects_limit(self, db):
        results = search_fts("knowledge", db, limit=1)
        assert len(results) <= 1

    def test_handles_missing_fts_index(self, tmp_path):
        db_path = tmp_path / "nofts.duckdb"
        init_schema(db_path)
        conn = get_connection(db_path)
        conn.execute(
            "INSERT INTO artifacts (id, file_name, file_type, content_hash, "
            "source_channel, raw_text) VALUES "
            "('a1', 'f.md', 'md', 'h', 'cli', 'some text')"
        )
        results = search_fts("some", conn)
        assert results == []
        conn.close()


class TestExtractSnippet:
    def test_extracts_around_term(self):
        text = "x" * 200 + " knowledge graph " + "y" * 200
        snippet = _extract_snippet(text, "knowledge")
        assert "knowledge" in snippet

    def test_short_text_returned_whole(self):
        assert _extract_snippet("short text", "short") == "short text"

    def test_no_match_returns_beginning(self):
        text = "A" * 300
        snippet = _extract_snippet(text, "zzz")
        assert snippet.startswith("A")
        assert snippet.endswith("...")
