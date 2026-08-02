"""Tests for resume, cover letter, and summary generators."""

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from twin.db import get_connection, init_schema
from twin.generators.cover_letter import generate_cover_letter
from twin.generators.resume import (
    _build_query,
    _extract_matched_skills,
    _identify_gaps,
    generate_resume,
)
from twin.generators.summary import (
    _format_label,
    _get_artifacts_in_range,
    generate_summary,
)
from twin.providers.llm import LLMResponse
from twin.retrieval.chunker import Chunk
from twin.retrieval.embeddings import embed_chunks
from twin.retrieval.fts import init_fts
from twin.synthesis.voice import create_profile


@pytest.fixture
def full_db(tmp_path: Path):
    db_path = tmp_path / "test.duckdb"
    chroma_path = tmp_path / "chroma"
    init_schema(db_path)
    conn = get_connection(db_path)

    conn.execute(
        "INSERT INTO nodes (id, type, name) VALUES "
        "('p1', 'project', 'Chitta'), "
        "('s1', 'skill', 'Python'), "
        "('s2', 'skill', 'Machine Learning')"
    )
    conn.execute(
        "INSERT INTO edges (id, source_id, target_id, type) VALUES ('e1', 'p1', 's1', 'USED_SKILL')"
    )
    conn.execute(
        "INSERT INTO artifacts (id, file_name, file_type, content_hash, "
        "source_channel, raw_text) VALUES "
        "('art_1', 'chitta.md', 'md', 'h1', 'cli', "
        "'Built Chitta knowledge graph system using Python')"
    )
    init_fts(conn)
    create_profile(conn, profile_text="Senior ML engineer.")
    chunks = [
        Chunk(
            id="c1",
            artifact_id="art_1",
            sequence=0,
            content="Built Chitta knowledge graph system using Python",
        ),
    ]
    embed_chunks(chunks, chroma_path)

    yield conn, chroma_path
    conn.close()


class TestResumeGenerator:
    def test_generates_resume(self, full_db):
        conn, chroma_path = full_db
        mock_router = MagicMock()
        mock_router.generate.return_value = LLMResponse(
            text="# Datta Vellal\n\n## Summary\nSenior engineer.",
            provider="gemini",
            model="flash",
        )
        result = generate_resume(
            conn,
            job_description="Python ML engineer",
            chroma_path=chroma_path,
            router=mock_router,
        )
        assert "Datta Vellal" in result.markdown
        assert result.evidence_used > 0
        mock_router.generate.assert_called_once()

    def test_skills_matched(self, full_db):
        conn, _ = full_db
        matched = _extract_matched_skills("Need Python and ML experience", conn)
        assert "Python" in matched

    def test_gaps_identified(self):
        matched = ["Python"]
        gaps = _identify_gaps("Need Python, Kubernetes, Docker", matched)
        assert "kubernetes" in gaps
        assert "docker" in gaps

    def test_build_query_with_jd(self):
        q = _build_query("Senior Python Engineer", ["ml", "nlp"])
        assert "Python" in q
        assert "ml" in q

    def test_build_query_default(self):
        q = _build_query("", None)
        assert "experience" in q


class TestCoverLetterGenerator:
    def test_generates_cover_letter(self, full_db):
        conn, chroma_path = full_db
        mock_router = MagicMock()
        mock_router.generate.return_value = LLMResponse(
            text="Dear Hiring Manager, I am excited...",
            provider="gemini",
            model="flash",
        )
        result = generate_cover_letter(
            conn,
            job_description="ML engineer role",
            company="Acme",
            role="Senior ML Engineer",
            chroma_path=chroma_path,
            router=mock_router,
        )
        assert "excited" in result.text
        assert result.evidence_used >= 0


class TestSummaryGenerator:
    def test_generates_summary(self, full_db):
        conn, _ = full_db
        mock_router = MagicMock()
        mock_router.generate.return_value = LLMResponse(
            text="## Summary\n\n### Completed\n- Built system",
            provider="gemini",
            model="flash",
        )
        result = generate_summary(
            conn,
            start="2026-01-01",
            end="2026-12-31",
            router=mock_router,
        )
        assert "Summary" in result.markdown
        assert result.time_range_label != ""

    def test_format_label_weekly(self):
        from datetime import datetime

        label = _format_label(datetime(2026, 7, 21), datetime(2026, 7, 27), "weekly")
        assert "July 21, 2026" in label

    def test_format_label_monthly(self):
        from datetime import datetime

        label = _format_label(datetime(2026, 7, 1), datetime(2026, 7, 31), "monthly")
        assert "July 2026" in label

    def test_artifacts_in_range(self, full_db):
        conn, _ = full_db
        arts = _get_artifacts_in_range(conn, "2020-01-01", "2030-12-31")
        assert len(arts) == 1
        assert arts[0]["file_name"] == "chitta.md"
