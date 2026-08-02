"""Tests for ChromaDB embedding storage and vector search."""

from pathlib import Path

import pytest

from twin.retrieval.chunker import Chunk
from twin.retrieval.embeddings import embed_chunks, get_client, get_collection, search_vectors


@pytest.fixture
def chroma_path(tmp_path: Path) -> Path:
    return tmp_path / "chroma"


class TestEmbedChunks:
    def test_embeds_chunks(self, chroma_path):
        chunks = [
            Chunk(id="c1", artifact_id="art_1", sequence=0, content="Python programming"),
            Chunk(id="c2", artifact_id="art_1", sequence=1, content="Machine learning"),
        ]
        count = embed_chunks(chunks, chroma_path)
        assert count == 2

        client = get_client(chroma_path)
        collection = get_collection(client)
        assert collection.count() == 2

    def test_empty_chunks_returns_zero(self, chroma_path):
        assert embed_chunks([], chroma_path) == 0

    def test_metadata_stored(self, chroma_path):
        chunks = [
            Chunk(
                id="c1",
                artifact_id="art_1",
                sequence=0,
                content="Test content",
                section="Intro",
            ),
        ]
        embed_chunks(chunks, chroma_path)

        client = get_client(chroma_path)
        collection = get_collection(client)
        result = collection.get(ids=["c1"], include=["metadatas"])
        assert result["metadatas"][0]["artifact_id"] == "art_1"
        assert result["metadatas"][0]["section"] == "Intro"


class TestSearchVectors:
    def test_search_returns_results(self, chroma_path):
        chunks = [
            Chunk(
                id="c1",
                artifact_id="art_1",
                sequence=0,
                content="I built a knowledge graph system using Python",
            ),
            Chunk(
                id="c2",
                artifact_id="art_1",
                sequence=1,
                content="The weather today is sunny and warm",
            ),
            Chunk(
                id="c3",
                artifact_id="art_2",
                sequence=0,
                content="Machine learning models for NLP tasks",
            ),
        ]
        embed_chunks(chunks, chroma_path)

        results = search_vectors("knowledge graph", n_results=2, chroma_path=chroma_path)
        assert len(results) == 2
        assert results[0]["id"] == "c1"  # Most relevant
        assert "content" in results[0]
        assert "distance" in results[0]

    def test_search_empty_collection(self, chroma_path):
        results = search_vectors("anything", chroma_path=chroma_path)
        assert results == []

    def test_search_with_metadata_filter(self, chroma_path):
        chunks = [
            Chunk(id="c1", artifact_id="art_1", sequence=0, content="Python code"),
            Chunk(id="c2", artifact_id="art_2", sequence=0, content="Python ML"),
        ]
        embed_chunks(chunks, chroma_path)

        results = search_vectors(
            "Python",
            n_results=5,
            chroma_path=chroma_path,
            where={"artifact_id": "art_2"},
        )
        assert len(results) == 1
        assert results[0]["id"] == "c2"

    def test_search_respects_n_results(self, chroma_path):
        chunks = [
            Chunk(id=f"c{i}", artifact_id="art_1", sequence=i, content=f"Content {i}")
            for i in range(5)
        ]
        embed_chunks(chunks, chroma_path)

        results = search_vectors("content", n_results=3, chroma_path=chroma_path)
        assert len(results) == 3
