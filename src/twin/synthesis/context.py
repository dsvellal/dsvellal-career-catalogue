"""Context assembly: gather relevant information for LLM synthesis."""

from dataclasses import dataclass, field
from pathlib import Path

import duckdb

from twin.retrieval.embeddings import DEFAULT_CHROMA_PATH, search_vectors
from twin.retrieval.fts import search_fts
from twin.retrieval.fusion import SearchResult, reciprocal_rank_fusion
from twin.retrieval.graph import build_graph, get_neighbors
from twin.synthesis.voice import build_system_prompt, get_active_profile


@dataclass
class AssembledContext:
    system_prompt: str
    evidence: list[dict] = field(default_factory=list)
    graph_context: list[dict] = field(default_factory=list)
    query: str = ""
    audience: str = "peer_engineer"


def assemble_context(
    query: str,
    conn: duckdb.DuckDBPyConnection,
    audience: str = "peer_engineer",
    top_k: int = 8,
    chroma_path: Path = DEFAULT_CHROMA_PATH,
    weights: dict[str, float] | None = None,
) -> AssembledContext:
    """Assemble full context for LLM synthesis from a user query.

    1. Hybrid search (vector + FTS + graph)
    2. Fuse via RRF
    3. Build system prompt from voice profile
    4. Return assembled context ready for LLM
    """
    profile = get_active_profile(conn)
    system_prompt = build_system_prompt(profile, audience)

    ranked_lists: dict[str, list[SearchResult]] = {}

    vector_results = _search_vectors(query, top_k, chroma_path)
    if vector_results:
        ranked_lists["vector"] = vector_results

    fts_results = _search_fts(query, conn, top_k)
    if fts_results:
        ranked_lists["fts"] = fts_results

    graph_results = _search_graph(query, conn, top_k)
    if graph_results:
        ranked_lists["graph"] = graph_results

    if weights is None:
        weights = {"vector": 1.0, "fts": 0.8, "graph": 0.6}

    fused = reciprocal_rank_fusion(ranked_lists, weights=weights, top_n=top_k)

    evidence = [
        {"id": r.id, "content": r.content, "score": r.score, "source": r.source} for r in fused
    ]

    graph_context = _get_graph_neighborhood(fused, conn)

    return AssembledContext(
        system_prompt=system_prompt,
        evidence=evidence,
        graph_context=graph_context,
        query=query,
        audience=audience,
    )


def format_context_for_llm(ctx: AssembledContext) -> str:
    """Format assembled context into a prompt section for the LLM."""
    parts = [f"Question: {ctx.query}\n"]

    if ctx.evidence:
        parts.append("Evidence:")
        for i, e in enumerate(ctx.evidence, 1):
            content_preview = e["content"][:300] if e["content"] else ""
            parts.append(f"  [{i}] {content_preview}")
        parts.append("")

    if ctx.graph_context:
        parts.append("Related knowledge graph nodes:")
        for node in ctx.graph_context[:10]:
            parts.append(f"  - {node.get('name', '')} ({node.get('type', '')})")
        parts.append("")

    parts.append(
        "Instructions: Answer the question using ONLY the evidence above. "
        "Cite evidence by number [1], [2], etc. "
        "If evidence is insufficient, say so honestly."
    )

    return "\n".join(parts)


def _search_vectors(query: str, top_k: int, chroma_path: Path) -> list[SearchResult]:
    try:
        hits = search_vectors(query, n_results=top_k, chroma_path=chroma_path)
    except Exception:
        return []
    return [
        SearchResult(
            id=h["id"],
            content=h["content"],
            source="vector",
            metadata=h.get("metadata", {}),
        )
        for h in hits
    ]


def _search_fts(query: str, conn: duckdb.DuckDBPyConnection, top_k: int) -> list[SearchResult]:
    try:
        hits = search_fts(query, conn, limit=top_k)
    except Exception:
        return []
    return [
        SearchResult(
            id=h["id"],
            content=h.get("snippet", ""),
            source="fts",
            metadata={"file_name": h.get("file_name", "")},
        )
        for h in hits
    ]


def _search_graph(query: str, conn: duckdb.DuckDBPyConnection, top_k: int) -> list[SearchResult]:
    """Search graph by matching query terms against node names."""
    terms = query.lower().split()
    try:
        nodes = conn.execute("SELECT id, type, name FROM nodes").fetchall()
    except Exception:
        return []

    scored = []
    for node_id, node_type, name in nodes:
        name_lower = name.lower()
        match_count = sum(1 for t in terms if t in name_lower)
        if match_count > 0:
            scored.append((match_count, node_id, node_type, name))

    scored.sort(reverse=True)
    return [
        SearchResult(
            id=node_id,
            content=f"{name} ({node_type})",
            source="graph",
            metadata={"type": node_type, "name": name},
        )
        for _, node_id, node_type, name in scored[:top_k]
    ]


def _get_graph_neighborhood(
    fused: list[SearchResult], conn: duckdb.DuckDBPyConnection
) -> list[dict]:
    """Get graph neighbors for top fused results that are graph nodes."""
    try:
        graph = build_graph(conn)
    except Exception:
        return []

    neighbors = []
    seen = set()
    for result in fused[:5]:
        node_id = result.metadata.get("artifact_id") or result.id
        for neighbor in get_neighbors(graph, node_id, depth=1):
            if neighbor["id"] not in seen:
                seen.add(neighbor["id"])
                neighbors.append(neighbor)

    return neighbors
