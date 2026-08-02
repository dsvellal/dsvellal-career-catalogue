"""Tests for context assembly pipeline."""

from pathlib import Path

import pytest

from twin.db import get_connection, init_schema
from twin.retrieval.chunker import Chunk
from twin.retrieval.embeddings import embed_chunks
from twin.retrieval.fts import init_fts
from twin.synthesis.context import assemble_context, format_context_for_llm
from twin.synthesis.voice import create_profile


@pytest.fixture
def full_db(tmp_path: Path):
    """DB with nodes, artifacts, FTS index, and embeddings."""
    db_path = tmp_path / "test.duckdb"
    chroma_path = tmp_path / "chroma"
    init_schema(db_path)
    conn = get_connection(db_path)

    conn.execute(
        "INSERT INTO nodes (id, type, name) VALUES "
        "('p1', 'project', 'Chitta'), "
        "('s1', 'skill', 'Python'), "
        "('s2', 'skill', 'Knowledge Graphs')"
    )
    conn.execute(
        "INSERT INTO edges (id, source_id, target_id, type) VALUES "
        "('e1', 'p1', 's1', 'USED_SKILL'), "
        "('e2', 'p1', 's2', 'USED_SKILL')"
    )
    conn.execute(
        "INSERT INTO artifacts (id, file_name, file_type, content_hash, "
        "source_channel, raw_text) VALUES "
        "('art_1', 'chitta.md', 'md', 'h1', 'cli', "
        "'I built Chitta, a knowledge graph system using Python and NLP')"
    )
    init_fts(conn)

    chunks = [
        Chunk(
            id="c1",
            artifact_id="art_1",
            sequence=0,
            content="I built Chitta, a knowledge graph system using Python and NLP",
        ),
    ]
    embed_chunks(chunks, chroma_path)

    create_profile(conn, profile_text="I am a senior ML engineer.")

    yield conn, chroma_path
    conn.close()


class TestAssembleContext:
    def test_returns_assembled_context(self, full_db):
        conn, chroma_path = full_db
        ctx = assemble_context("knowledge graph", conn, chroma_path=chroma_path)
        assert ctx.query == "knowledge graph"
        assert ctx.system_prompt != ""
        assert "Datta Vellal" in ctx.system_prompt

    def test_includes_evidence(self, full_db):
        conn, chroma_path = full_db
        ctx = assemble_context("knowledge graph Python", conn, chroma_path=chroma_path)
        assert len(ctx.evidence) > 0

    def test_includes_system_prompt_with_voice(self, full_db):
        conn, chroma_path = full_db
        ctx = assemble_context("anything", conn, chroma_path=chroma_path)
        assert "senior ML engineer" in ctx.system_prompt

    def test_works_without_chroma(self, full_db, tmp_path):
        conn, _ = full_db
        empty_chroma = tmp_path / "empty_chroma"
        ctx = assemble_context("knowledge graph", conn, chroma_path=empty_chroma)
        # Should still work via FTS and graph
        assert ctx.system_prompt != ""

    def test_custom_weights(self, full_db):
        conn, chroma_path = full_db
        ctx = assemble_context(
            "Python",
            conn,
            chroma_path=chroma_path,
            weights={"vector": 0.0, "fts": 1.0, "graph": 0.0},
        )
        assert ctx.evidence is not None


class TestFormatContextForLLM:
    def test_includes_query(self, full_db):
        conn, chroma_path = full_db
        ctx = assemble_context("knowledge graph", conn, chroma_path=chroma_path)
        formatted = format_context_for_llm(ctx)
        assert "knowledge graph" in formatted

    def test_includes_evidence_citations(self, full_db):
        conn, chroma_path = full_db
        ctx = assemble_context("knowledge graph Python", conn, chroma_path=chroma_path)
        formatted = format_context_for_llm(ctx)
        assert "[1]" in formatted

    def test_includes_instructions(self, full_db):
        conn, chroma_path = full_db
        ctx = assemble_context("test", conn, chroma_path=chroma_path)
        formatted = format_context_for_llm(ctx)
        assert "ONLY the evidence" in formatted

    def test_handles_empty_context(self):
        from twin.synthesis.context import AssembledContext

        ctx = AssembledContext(system_prompt="test", query="hello")
        formatted = format_context_for_llm(ctx)
        assert "hello" in formatted
