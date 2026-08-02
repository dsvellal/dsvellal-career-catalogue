"""Tests for text chunking."""

from pathlib import Path

import pytest

from twin.db import get_connection, init_schema
from twin.retrieval.chunker import Chunk, chunk_text, store_chunks


class TestChunkText:
    def test_empty_text_returns_no_chunks(self):
        assert chunk_text("", "art_1") == []
        assert chunk_text("   \n  ", "art_1") == []

    def test_short_text_single_chunk(self):
        chunks = chunk_text("Hello world.", "art_1")
        assert len(chunks) == 1
        assert chunks[0].content == "Hello world."
        assert chunks[0].artifact_id == "art_1"
        assert chunks[0].sequence == 0

    def test_respects_chunk_size(self):
        text = ". ".join([f"Sentence number {i}" for i in range(50)]) + "."
        chunks = chunk_text(text, "art_1", chunk_size=100, overlap=0)
        assert len(chunks) > 1

    def test_preserves_sections(self):
        text = "# Intro\n\nFirst paragraph.\n\n# Skills\n\nPython and ML."
        chunks = chunk_text(text, "art_1")
        sections = [c.section for c in chunks]
        assert "Intro" in sections
        assert "Skills" in sections

    def test_sequence_numbers_increment(self):
        text = "\n\n".join([f"Paragraph {i}." for i in range(20)])
        chunks = chunk_text(text, "art_1", chunk_size=50, overlap=0)
        for i, chunk in enumerate(chunks):
            assert chunk.sequence == i

    def test_text_without_headers(self):
        text = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        chunks = chunk_text(text, "art_1")
        assert len(chunks) >= 1
        assert chunks[0].section == ""

    def test_overlap_included(self):
        para_a = "A" * 100
        para_b = "B" * 100
        para_c = "C" * 100
        text = f"{para_a}\n\n{para_b}\n\n{para_c}"
        chunks = chunk_text(text, "art_1", chunk_size=150, overlap=30)
        if len(chunks) > 1:
            # Second chunk should contain some overlap from the first
            assert len(chunks[1].content) > 100

    def test_chunk_ids_are_unique(self):
        text = "\n\n".join([f"Paragraph {i}." for i in range(10)])
        chunks = chunk_text(text, "art_1", chunk_size=30, overlap=0)
        ids = [c.id for c in chunks]
        assert len(ids) == len(set(ids))


class TestStoreChunks:
    @pytest.fixture
    def db(self, tmp_path: Path):
        db_path = tmp_path / "test.duckdb"
        init_schema(db_path)
        conn = get_connection(db_path)
        conn.execute(
            "INSERT INTO artifacts (id, file_name, file_type, content_hash, source_channel) "
            "VALUES ('art_1', 'test.md', 'md', 'hash123', 'cli')"
        )
        yield conn
        conn.close()

    def test_stores_chunks_in_db(self, db):
        chunks = [
            Chunk(id="c1", artifact_id="art_1", sequence=0, content="Hello"),
            Chunk(id="c2", artifact_id="art_1", sequence=1, content="World"),
        ]
        count = store_chunks(chunks, db)
        assert count == 2
        rows = db.execute("SELECT id, content, sequence FROM chunks ORDER BY sequence").fetchall()
        assert rows == [("c1", "Hello", 0), ("c2", "World", 1)]

    def test_updates_artifact_chunk_count(self, db):
        chunks = [
            Chunk(id="c1", artifact_id="art_1", sequence=0, content="Hello"),
            Chunk(id="c2", artifact_id="art_1", sequence=1, content="World"),
            Chunk(id="c3", artifact_id="art_1", sequence=2, content="Foo"),
        ]
        store_chunks(chunks, db)
        row = db.execute("SELECT chunk_count FROM artifacts WHERE id = 'art_1'").fetchone()
        assert row[0] == 3

    def test_empty_chunks_returns_zero(self, db):
        count = store_chunks([], db)
        assert count == 0
