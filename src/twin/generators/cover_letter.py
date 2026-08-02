"""Cover letter generator: produce tailored cover letters from the knowledge graph."""

from dataclasses import dataclass
from pathlib import Path

import duckdb

from twin.providers.llm import LLMResponse, ProviderRouter
from twin.retrieval.embeddings import DEFAULT_CHROMA_PATH
from twin.synthesis.context import assemble_context

COVER_LETTER_SYSTEM = """\
You are writing a cover letter as Datta Vellal, in first person.

Rules:
- Write in first person ("I", "my")
- Be professional but personable
- Connect specific experience to the role requirements
- Show genuine enthusiasm without being sycophantic
- Keep it to 3-4 paragraphs (300-400 words)
- Only claim things supported by the evidence provided
- End with a clear call to action
"""

COVER_LETTER_PROMPT = """\
Write a cover letter for the following job:

Company: {company}
Role: {role}

Job Description:
{job_description}

My relevant experience (from knowledge graph):
{evidence}

Related projects and skills:
{graph_context}

Write ONLY the cover letter body (no addresses/dates). Start with a compelling opening.
"""


@dataclass
class CoverLetterResult:
    text: str
    evidence_used: int = 0


def generate_cover_letter(
    conn: duckdb.DuckDBPyConnection,
    job_description: str,
    company: str = "",
    role: str = "",
    chroma_path: Path = DEFAULT_CHROMA_PATH,
    router: ProviderRouter | None = None,
) -> CoverLetterResult:
    """Generate a tailored cover letter."""
    ctx = assemble_context(
        job_description[:500],
        conn,
        audience="hiring_manager",
        chroma_path=chroma_path,
        weights={"vector": 1.0, "fts": 0.5, "graph": 0.8},
    )

    evidence_text = "\n".join(f"- {e['content'][:200]}" for e in ctx.evidence)
    graph_text = "\n".join(
        f"- {n.get('name', '')} ({n.get('type', '')})" for n in ctx.graph_context[:10]
    )

    prompt = COVER_LETTER_PROMPT.format(
        company=company or "the company",
        role=role or "the role",
        job_description=job_description,
        evidence=evidence_text,
        graph_context=graph_text,
    )

    if router is None:
        router = ProviderRouter()

    response: LLMResponse = router.generate(
        prompt=prompt,
        system=COVER_LETTER_SYSTEM,
        temperature=0.6,
    )

    return CoverLetterResult(text=response.text, evidence_used=len(ctx.evidence))
