"""Tests for the FastAPI /api/ask endpoint."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from twin.api.app import app
from twin.db import get_connection, init_schema
from twin.providers.llm import LLMResponse
from twin.retrieval.chunker import Chunk
from twin.retrieval.embeddings import embed_chunks
from twin.retrieval.fts import init_fts
from twin.synthesis.voice import create_profile


@pytest.fixture
def full_setup(tmp_path: Path):
    """Full setup with DB, chroma, FTS, and voice profile."""
    db_path = tmp_path / "test.duckdb"
    chroma_path = tmp_path / "chroma"

    init_schema(db_path)
    conn = get_connection(db_path)

    conn.execute(
        "INSERT INTO nodes (id, type, name) VALUES "
        "('p1', 'project', 'Chitta'), "
        "('s1', 'skill', 'Python')"
    )
    conn.execute(
        "INSERT INTO edges (id, source_id, target_id, type) VALUES ('e1', 'p1', 's1', 'USED_SKILL')"
    )
    conn.execute(
        "INSERT INTO artifacts (id, file_name, file_type, content_hash, "
        "source_channel, raw_text) VALUES "
        "('art_1', 'chitta.md', 'md', 'h1', 'cli', "
        "'I built Chitta using Python and knowledge graphs')"
    )
    init_fts(conn)
    create_profile(conn, profile_text="I am a senior engineer.")

    chunks = [
        Chunk(
            id="c1",
            artifact_id="art_1",
            sequence=0,
            content="I built Chitta using Python and knowledge graphs",
        ),
    ]
    embed_chunks(chunks, chroma_path)

    conn.close()
    return db_path, chroma_path


@pytest.fixture
def client():
    return TestClient(app)


class TestAskEndpoint:
    def test_ask_returns_answer(self, client, full_setup):
        db_path, chroma_path = full_setup

        mock_llm = MagicMock()
        mock_llm.generate.return_value = LLMResponse(
            text="I built Chitta, a knowledge graph system.",
            provider="gemini",
            model="flash",
        )

        with (
            patch("twin.api.app.is_initialized", return_value=True),
            patch("twin.api.app.get_connection") as mock_conn,
            patch("twin.api.app.ProviderRouter", return_value=mock_llm),
            patch("twin.api.app.DEFAULT_CHROMA_PATH", chroma_path),
        ):
            mock_conn.return_value = get_connection(db_path)
            response = client.post(
                "/api/ask",
                json={
                    "question": "What is Chitta?",
                    "context": {"audience": "peer_engineer"},
                },
            )

        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert data["answer"] == "I built Chitta, a knowledge graph system."
        assert data["provider"] == "gemini"

    def test_ask_returns_citations(self, client, full_setup):
        db_path, chroma_path = full_setup

        mock_llm = MagicMock()
        mock_llm.generate.return_value = LLMResponse(
            text="Answer.",
            provider="gemini",
            model="flash",
        )

        with (
            patch("twin.api.app.is_initialized", return_value=True),
            patch("twin.api.app.get_connection") as mock_conn,
            patch("twin.api.app.ProviderRouter", return_value=mock_llm),
            patch("twin.api.app.DEFAULT_CHROMA_PATH", chroma_path),
        ):
            mock_conn.return_value = get_connection(db_path)
            response = client.post("/api/ask", json={"question": "Python skills"})

        data = response.json()
        assert "citations" in data

    def test_ask_503_when_not_initialized(self, client):
        with patch("twin.api.app.is_initialized", return_value=False):
            response = client.post("/api/ask", json={"question": "test"})
        assert response.status_code == 503

    def test_ask_validates_request(self, client):
        with patch("twin.api.app.is_initialized", return_value=True):
            response = client.post("/api/ask", json={})
        assert response.status_code == 422


class TestHealthEndpoint:
    def test_health_ok(self, client):
        with patch("twin.api.app.is_initialized", return_value=True):
            response = client.get("/api/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"

    def test_health_not_initialized(self, client):
        with patch("twin.api.app.is_initialized", return_value=False):
            response = client.get("/api/health")
        assert response.status_code == 200
        assert response.json()["status"] == "not_initialized"


class TestMediaEndpoint:
    def test_serves_local_file(self, client, tmp_path):
        db_path = tmp_path / "test.duckdb"
        media_dir = tmp_path / "media"
        media_dir.mkdir()
        img = media_dir / "abc123.jpg"
        img.write_bytes(b"\xff\xd8\xff\xe0" + b"\x00" * 100)

        init_schema(db_path)
        conn = get_connection(db_path)
        conn.execute(
            "INSERT INTO artifacts (id, file_name, file_type, content_hash, "
            "source_channel, media_path) VALUES "
            "('art_media', 'cert.jpg', 'jpg', 'abc123', 'cli', 'abc123.jpg')"
        )
        conn.close()

        with (
            patch("twin.api.app.is_initialized", return_value=True),
            patch("twin.api.app.get_connection") as mock_conn,
            patch("twin.api.app.DEFAULT_MEDIA_DIR", media_dir),
        ):
            mock_conn.return_value = get_connection(db_path)
            response = client.get("/api/media/art_media")

        assert response.status_code == 200
        assert response.headers["content-type"] == "image/jpeg"

    def test_redirects_to_media_url(self, client, tmp_path):
        db_path = tmp_path / "test.duckdb"
        media_dir = tmp_path / "media"
        media_dir.mkdir()

        init_schema(db_path)
        conn = get_connection(db_path)
        conn.execute(
            "INSERT INTO artifacts (id, file_name, file_type, content_hash, "
            "source_channel, media_url) VALUES "
            "('art_url', 'cert.jpg', 'jpg', 'nolocalfile', 'cli', "
            "'https://example.com/image.jpg')"
        )
        conn.close()

        with (
            patch("twin.api.app.is_initialized", return_value=True),
            patch("twin.api.app.get_connection") as mock_conn,
            patch("twin.api.app.DEFAULT_MEDIA_DIR", media_dir),
        ):
            mock_conn.return_value = get_connection(db_path)
            response = client.get("/api/media/art_url", follow_redirects=False)

        assert response.status_code == 302
        assert response.headers["location"] == "https://example.com/image.jpg"

    def test_404_for_missing_artifact(self, client, tmp_path):
        db_path = tmp_path / "test.duckdb"
        init_schema(db_path)

        with (
            patch("twin.api.app.is_initialized", return_value=True),
            patch("twin.api.app.get_connection") as mock_conn,
        ):
            mock_conn.return_value = get_connection(db_path)
            response = client.get("/api/media/nonexistent")

        assert response.status_code == 404

    def test_404_when_no_media_available(self, client, tmp_path):
        db_path = tmp_path / "test.duckdb"
        media_dir = tmp_path / "media"
        media_dir.mkdir()

        init_schema(db_path)
        conn = get_connection(db_path)
        conn.execute(
            "INSERT INTO artifacts (id, file_name, file_type, content_hash, "
            "source_channel) VALUES "
            "('art_nomedia', 'notes.md', 'md', 'hashonly', 'cli')"
        )
        conn.close()

        with (
            patch("twin.api.app.is_initialized", return_value=True),
            patch("twin.api.app.get_connection") as mock_conn,
            patch("twin.api.app.DEFAULT_MEDIA_DIR", media_dir),
        ):
            mock_conn.return_value = get_connection(db_path)
            response = client.get("/api/media/art_nomedia")

        assert response.status_code == 404
