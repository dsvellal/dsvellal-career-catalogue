"""Full-text search using DuckDB's FTS extension."""

import duckdb


def init_fts(conn: duckdb.DuckDBPyConnection) -> None:
    """Install and load FTS extension, create index on artifacts.raw_text."""
    conn.execute("INSTALL fts")
    conn.execute("LOAD fts")
    conn.execute("PRAGMA create_fts_index('artifacts', 'id', 'raw_text', 'file_name', overwrite=1)")


def search_fts(
    query: str,
    conn: duckdb.DuckDBPyConnection,
    limit: int = 10,
) -> list[dict]:
    """Full-text search over artifacts. Returns list of {id, file_name, score, snippet}."""
    if not query.strip():
        return []

    try:
        rows = conn.execute(
            "SELECT id, file_name, raw_text, fts_main_artifacts.match_bm25(id, ?) AS score "
            "FROM artifacts "
            "WHERE score IS NOT NULL "
            "ORDER BY score DESC "
            "LIMIT ?",
            [query, limit],
        ).fetchall()
    except duckdb.CatalogException:
        return []

    results = []
    for row in rows:
        artifact_id, file_name, raw_text, score = row
        snippet = _extract_snippet(raw_text or "", query)
        results.append(
            {
                "id": artifact_id,
                "file_name": file_name,
                "score": score,
                "snippet": snippet,
            }
        )
    return results


def _extract_snippet(text: str, query: str, window: int = 150) -> str:
    """Extract a text snippet around the first occurrence of query terms."""
    lower_text = text.lower()
    terms = query.lower().split()

    best_pos = -1
    for term in terms:
        pos = lower_text.find(term)
        if pos >= 0:
            best_pos = pos
            break

    if best_pos < 0:
        return text[:window] + "..." if len(text) > window else text

    start = max(0, best_pos - window // 2)
    end = min(len(text), best_pos + window)
    snippet = text[start:end]

    if start > 0:
        snippet = "..." + snippet
    if end < len(text):
        snippet = snippet + "..."

    return snippet
