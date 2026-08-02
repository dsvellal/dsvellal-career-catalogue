"""ChromaDB integration for embedding storage and vector search."""

from pathlib import Path

import chromadb

from twin.retrieval.chunker import Chunk

DEFAULT_CHROMA_PATH = Path("./data/chroma")
COLLECTION_NAME = "twin_chunks"


def get_client(chroma_path: Path = DEFAULT_CHROMA_PATH) -> chromadb.ClientAPI:
    """Get a persistent ChromaDB client."""
    chroma_path.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(chroma_path))


def get_collection(client: chromadb.ClientAPI) -> chromadb.Collection:
    """Get or create the chunks collection."""
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )


def embed_chunks(chunks: list[Chunk], chroma_path: Path = DEFAULT_CHROMA_PATH) -> int:
    """Embed and store chunks in ChromaDB. Returns count embedded.

    Uses ChromaDB's built-in default embedding function.
    """
    if not chunks:
        return 0

    client = get_client(chroma_path)
    collection = get_collection(client)

    ids = [c.id for c in chunks]
    documents = [c.content for c in chunks]
    metadatas = [
        {"artifact_id": c.artifact_id, "sequence": c.sequence, "section": c.section} for c in chunks
    ]

    collection.add(ids=ids, documents=documents, metadatas=metadatas)  # type: ignore[arg-type]
    return len(chunks)


def search_vectors(
    query: str,
    n_results: int = 10,
    chroma_path: Path = DEFAULT_CHROMA_PATH,
    where: dict | None = None,
) -> list[dict]:
    """Search for similar chunks. Returns list of {id, content, metadata, distance}."""
    client = get_client(chroma_path)
    collection = get_collection(client)

    if collection.count() == 0:
        return []

    kwargs: dict = {"query_texts": [query], "n_results": min(n_results, collection.count())}
    if where:
        kwargs["where"] = where

    results = collection.query(**kwargs)

    hits = []
    for i in range(len(results["ids"][0])):
        hits.append(
            {
                "id": results["ids"][0][i],
                "content": results["documents"][0][i] if results["documents"] else "",
                "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                "distance": results["distances"][0][i] if results["distances"] else 0.0,
            }
        )
    return hits
