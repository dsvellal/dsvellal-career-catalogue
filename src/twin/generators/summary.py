"""Weekly/monthly summary generator from ingested artifacts and graph activity."""

from dataclasses import dataclass, field
from datetime import datetime

import duckdb

from twin.providers.llm import LLMResponse, ProviderRouter

SUMMARY_SYSTEM = """\
You are generating a work summary for Datta Vellal, in first person.

Rules:
- Use first person
- Be concise and action-oriented
- Group by: completed, in-progress, follow-ups
- Include specific project names and outcomes where available
- If evidence is thin, say so honestly rather than padding
"""

SUMMARY_PROMPT = """\
Generate a {format} summary for the period: {start} to {end}.

Artifacts ingested during this period:
{artifacts}

Nodes created/updated during this period:
{nodes}

Format as:
## Summary ({label})

### Completed
- [bullet points]

### In Progress
- [bullet points]

### Follow-ups
- [bullet points]

Output ONLY the markdown summary.
"""


@dataclass
class SummaryResult:
    markdown: str
    time_range_label: str
    artifacts_referenced: int = 0
    sections: dict = field(default_factory=dict)


def generate_summary(
    conn: duckdb.DuckDBPyConnection,
    start: str,
    end: str,
    format_type: str = "weekly",
    router: ProviderRouter | None = None,
) -> SummaryResult:
    """Generate a time-bounded work summary."""
    start_dt = datetime.fromisoformat(start)
    end_dt = datetime.fromisoformat(end)
    label = _format_label(start_dt, end_dt, format_type)

    artifacts = _get_artifacts_in_range(conn, start, end)
    nodes = _get_nodes_in_range(conn, start, end)

    artifacts_text = (
        "\n".join(
            f"- {a['file_name']} ({a['file_type']}) — ingested {a['date']}" for a in artifacts
        )
        or "No artifacts ingested in this period."
    )

    nodes_text = (
        "\n".join(f"- {n['name']} ({n['type']})" for n in nodes)
        or "No new nodes created in this period."
    )

    prompt = SUMMARY_PROMPT.format(
        format=format_type,
        start=start,
        end=end,
        artifacts=artifacts_text,
        nodes=nodes_text,
        label=label,
    )

    if router is None:
        router = ProviderRouter()

    response: LLMResponse = router.generate(
        prompt=prompt,
        system=SUMMARY_SYSTEM,
        temperature=0.4,
    )

    return SummaryResult(
        markdown=response.text,
        time_range_label=label,
        artifacts_referenced=len(artifacts),
    )


def _get_artifacts_in_range(conn: duckdb.DuckDBPyConnection, start: str, end: str) -> list[dict]:
    rows = conn.execute(
        "SELECT file_name, file_type, ingested_at FROM artifacts "
        "WHERE ingested_at >= ? AND ingested_at <= ? "
        "ORDER BY ingested_at",
        [start, end],
    ).fetchall()
    return [{"file_name": r[0], "file_type": r[1], "date": str(r[2])[:10]} for r in rows]


def _get_nodes_in_range(conn: duckdb.DuckDBPyConnection, start: str, end: str) -> list[dict]:
    rows = conn.execute(
        "SELECT name, type FROM nodes "
        "WHERE created_at >= ? AND created_at <= ? "
        "ORDER BY created_at",
        [start, end],
    ).fetchall()
    return [{"name": r[0], "type": r[1]} for r in rows]


def _format_label(start: datetime, end: datetime, format_type: str) -> str:
    if format_type == "weekly":
        return f"Week of {start.strftime('%B %d, %Y')}"
    elif format_type == "monthly":
        return start.strftime("%B %Y")
    return f"{start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}"
