"""Resume generator: produce tailored markdown resumes from the knowledge graph."""

from dataclasses import dataclass, field
from pathlib import Path

import duckdb

from twin.providers.llm import LLMResponse, ProviderRouter
from twin.retrieval.embeddings import DEFAULT_CHROMA_PATH
from twin.synthesis.context import assemble_context

RESUME_SYSTEM_PROMPT = """\
You are generating a professional resume for Datta Vellal.

Rules:
- Use third person ("Datta Vellal" or "Experienced engineer who...")
- Use concise bullet points for experience
- Quantify impact where evidence supports it
- Only include claims supported by the provided evidence
- Structure: Summary, Experience, Skills, Education, Achievements
- Be concise — aim for 1-2 pages worth of content
- Tailor to the job description if provided
"""

RESUME_PROMPT_TEMPLATE = """\
Generate a professional resume in markdown format.

{jd_section}

Evidence from knowledge graph:
{evidence}

Related skills and projects:
{graph_context}

Format the resume with these sections:
# [Name]

## Summary
[2-3 sentence professional summary tailored to the role]

## Experience
[Reverse chronological, bullet points with metrics]

## Skills
[Categorized: Technical, Tools, Methodologies]

## Achievements
[Awards, certifications, recognition]

Output ONLY the markdown resume, no commentary.
"""


@dataclass
class ResumeResult:
    markdown: str
    skills_matched: list[str] = field(default_factory=list)
    evidence_used: int = 0
    gaps: list[str] = field(default_factory=list)


def generate_resume(
    conn: duckdb.DuckDBPyConnection,
    job_description: str = "",
    emphasis: list[str] | None = None,
    chroma_path: Path = DEFAULT_CHROMA_PATH,
    router: ProviderRouter | None = None,
) -> ResumeResult:
    """Generate a tailored resume based on the knowledge graph and optional JD."""
    query = _build_query(job_description, emphasis)

    ctx = assemble_context(
        query,
        conn,
        audience="technical_recruiter",
        chroma_path=chroma_path,
        weights={"vector": 1.2, "fts": 0.6, "graph": 1.0},
    )

    evidence_text = "\n".join(
        f"- [{i + 1}] {e['content'][:200]}" for i, e in enumerate(ctx.evidence)
    )
    graph_text = "\n".join(
        f"- {n.get('name', '')} ({n.get('type', '')})" for n in ctx.graph_context[:15]
    )

    jd_section = ""
    if job_description:
        jd_section = f"Target Job Description:\n{job_description}\n"

    prompt = RESUME_PROMPT_TEMPLATE.format(
        jd_section=jd_section,
        evidence=evidence_text,
        graph_context=graph_text,
    )

    if router is None:
        router = ProviderRouter()

    response: LLMResponse = router.generate(
        prompt=prompt,
        system=RESUME_SYSTEM_PROMPT,
        temperature=0.3,
    )

    skills_matched = _extract_matched_skills(job_description, conn)
    gaps = _identify_gaps(job_description, skills_matched)

    return ResumeResult(
        markdown=response.text,
        skills_matched=skills_matched,
        evidence_used=len(ctx.evidence),
        gaps=gaps,
    )


def _build_query(job_description: str, emphasis: list[str] | None) -> str:
    parts = []
    if job_description:
        parts.append(job_description[:500])
    if emphasis:
        parts.append(" ".join(emphasis))
    return " ".join(parts) if parts else "professional experience projects skills achievements"


def _extract_matched_skills(jd: str, conn: duckdb.DuckDBPyConnection) -> list[str]:
    """Find skills in the graph that match the JD."""
    if not jd:
        return []
    jd_lower = jd.lower()
    rows = conn.execute("SELECT name FROM nodes WHERE type = 'skill'").fetchall()
    return [name for (name,) in rows if name.lower() in jd_lower]


def _identify_gaps(jd: str, matched: list[str]) -> list[str]:
    """Identify JD requirements that aren't evidenced in the graph."""
    if not jd:
        return []
    common_skills = [
        "python",
        "java",
        "kubernetes",
        "docker",
        "aws",
        "gcp",
        "azure",
        "react",
        "typescript",
        "sql",
        "machine learning",
        "deep learning",
        "nlp",
        "data engineering",
        "ci/cd",
        "terraform",
        "go",
        "rust",
    ]
    jd_lower = jd.lower()
    matched_lower = {s.lower() for s in matched}
    return [s for s in common_skills if s in jd_lower and s not in matched_lower]
