"""Reciprocal Rank Fusion (RRF) for combining multiple retrieval strategies."""

from dataclasses import dataclass, field


@dataclass
class SearchResult:
    id: str
    content: str = ""
    score: float = 0.0
    source: str = ""
    metadata: dict = field(default_factory=dict)


DEFAULT_K = 60  # RRF constant


def reciprocal_rank_fusion(
    ranked_lists: dict[str, list[SearchResult]],
    weights: dict[str, float] | None = None,
    k: int = DEFAULT_K,
    top_n: int = 10,
) -> list[SearchResult]:
    """Fuse multiple ranked result lists using weighted RRF.

    Args:
        ranked_lists: {source_name: [results ordered by relevance]}
        weights: {source_name: weight}. Defaults to equal weights.
        k: RRF constant (higher = less emphasis on top ranks)
        top_n: number of results to return

    Returns:
        Fused results sorted by combined RRF score.
    """
    if not ranked_lists:
        return []

    if weights is None:
        weights = {name: 1.0 for name in ranked_lists}

    scores: dict[str, float] = {}
    items: dict[str, SearchResult] = {}

    for source_name, results in ranked_lists.items():
        weight = weights.get(source_name, 1.0)
        for rank, result in enumerate(results):
            rrf_score = weight / (k + rank + 1)
            scores[result.id] = scores.get(result.id, 0.0) + rrf_score
            if result.id not in items or len(result.content) > len(items[result.id].content):
                items[result.id] = result

    fused = []
    for result_id, score in sorted(scores.items(), key=lambda x: -x[1]):
        result = items[result_id]
        fused.append(
            SearchResult(
                id=result.id,
                content=result.content,
                score=score,
                source=result.source,
                metadata=result.metadata,
            )
        )

    return fused[:top_n]
