"""FastAPI application: /api/ask, /api/generate, /api/summary, /api/media, graph, chat."""

import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse, Response
from pydantic import BaseModel, Field

from twin.db import DEFAULT_DB_PATH, get_connection, is_initialized
from twin.generators.cover_letter import generate_cover_letter
from twin.generators.resume import generate_resume
from twin.generators.summary import generate_summary
from twin.media import DEFAULT_MEDIA_DIR, get_content_type, get_media_path
from twin.providers.llm import LLMResponse, ProviderRouter
from twin.retrieval.embeddings import DEFAULT_CHROMA_PATH
from twin.synthesis.context import assemble_context, format_context_for_llm

app = FastAPI(title="Twin API", version="0.1.0")

TEMPLATES_DIR = Path(__file__).parent.parent.parent.parent / "templates"


@app.get("/", response_class=HTMLResponse)
def chat_ui() -> HTMLResponse:
    """Serve the chat interface."""
    chat_html = TEMPLATES_DIR / "chat.html"
    return HTMLResponse(content=chat_html.read_text())


class AskRequest(BaseModel):
    question: str
    context: dict = Field(default_factory=dict)


class Citation(BaseModel):
    id: str
    content: str = ""
    score: float = 0.0
    source: str = ""


class AskResponse(BaseModel):
    answer: str
    citations: list[Citation] = []
    confidence: float = 0.0
    provider: str = ""


@app.post("/api/ask", response_model=AskResponse)
def ask(
    request: AskRequest,
    db_path: Path = DEFAULT_DB_PATH,
    chroma_path: Path = DEFAULT_CHROMA_PATH,
) -> AskResponse:
    """Answer a question using the knowledge graph and LLM synthesis."""
    if not is_initialized(db_path):
        raise HTTPException(status_code=503, detail="Database not initialized")

    audience = request.context.get("audience", "peer_engineer")

    conn = get_connection(db_path)
    try:
        ctx = assemble_context(request.question, conn, audience=audience, chroma_path=chroma_path)

        user_prompt = format_context_for_llm(ctx)

        router = ProviderRouter()
        llm_response: LLMResponse = router.generate(
            prompt=user_prompt,
            system=ctx.system_prompt,
            temperature=0.7,
        )

        citations = [
            Citation(id=e["id"], content=e["content"][:200], score=e["score"], source=e["source"])
            for e in ctx.evidence
        ]

        confidence = _estimate_confidence(ctx.evidence)

        return AskResponse(
            answer=llm_response.text,
            citations=citations,
            confidence=confidence,
            provider=llm_response.provider,
        )
    finally:
        conn.close()


@app.get("/api/health")
def health() -> dict:
    """Health check endpoint."""
    initialized = is_initialized(DEFAULT_DB_PATH)
    return {"status": "ok" if initialized else "not_initialized", "db": str(DEFAULT_DB_PATH)}


class GenerateRequest(BaseModel):
    type: str = "resume"
    job_description: str = ""
    company: str = ""
    role: str = ""
    emphasis: list[str] = Field(default_factory=list)
    format: str = "markdown"


class GenerateResponse(BaseModel):
    content: str
    format: str = "markdown"
    metadata: dict = Field(default_factory=dict)


@app.post("/api/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest) -> GenerateResponse:
    """Generate structured output (resume or cover letter)."""
    if not is_initialized(DEFAULT_DB_PATH):
        raise HTTPException(status_code=503, detail="Database not initialized")

    conn = get_connection(DEFAULT_DB_PATH)
    try:
        if request.type == "resume":
            result = generate_resume(
                conn,
                job_description=request.job_description,
                emphasis=request.emphasis or None,
            )
            return GenerateResponse(
                content=result.markdown,
                format="markdown",
                metadata={
                    "skills_matched": result.skills_matched,
                    "evidence_used": result.evidence_used,
                    "gaps": result.gaps,
                },
            )
        elif request.type == "cover_letter":
            cl_result = generate_cover_letter(
                conn,
                job_description=request.job_description,
                company=request.company,
                role=request.role,
            )
            return GenerateResponse(
                content=cl_result.text,
                format="markdown",
                metadata={"evidence_used": cl_result.evidence_used},
            )
        else:
            raise HTTPException(status_code=400, detail=f"Unknown type: {request.type}")
    finally:
        conn.close()


class SummaryRequest(BaseModel):
    time_range: dict = Field(default_factory=dict)
    format: str = "weekly"


class SummaryResponse(BaseModel):
    summary: str
    time_range_label: str = ""
    artifacts_referenced: int = 0


@app.post("/api/summary", response_model=SummaryResponse)
def summary(request: SummaryRequest) -> SummaryResponse:
    """Generate a time-bounded work summary."""
    if not is_initialized(DEFAULT_DB_PATH):
        raise HTTPException(status_code=503, detail="Database not initialized")

    start = request.time_range.get("start", "")
    end = request.time_range.get("end", "")
    if not start or not end:
        raise HTTPException(status_code=400, detail="time_range.start and .end required")

    conn = get_connection(DEFAULT_DB_PATH)
    try:
        result = generate_summary(conn, start=start, end=end, format_type=request.format)
        return SummaryResponse(
            summary=result.markdown,
            time_range_label=result.time_range_label,
            artifacts_referenced=result.artifacts_referenced,
        )
    finally:
        conn.close()


@app.get("/api/media/{artifact_id}", response_model=None)
def media(artifact_id: str) -> Response:
    """Serve the original media file for an artifact, or redirect to its cloud URL."""
    if not is_initialized(DEFAULT_DB_PATH):
        raise HTTPException(status_code=503, detail="Database not initialized")

    conn = get_connection(DEFAULT_DB_PATH)
    try:
        row = conn.execute(
            "SELECT content_hash, media_path, media_url FROM artifacts WHERE id = ?",
            [artifact_id],
        ).fetchone()
    finally:
        conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Artifact not found")

    content_hash, media_path_str, media_url = row

    if media_url:
        local = get_media_path(content_hash, DEFAULT_MEDIA_DIR)
        if local and local.exists():
            return FileResponse(str(local), media_type=get_content_type(local))
        return RedirectResponse(url=media_url, status_code=302)

    if media_path_str:
        local = DEFAULT_MEDIA_DIR / media_path_str
        if local.exists():
            return FileResponse(str(local), media_type=get_content_type(local))

    local = get_media_path(content_hash, DEFAULT_MEDIA_DIR)
    if local and local.exists():
        return FileResponse(str(local), media_type=get_content_type(local))

    raise HTTPException(status_code=404, detail="Media file not found")


@app.get("/api/graph")
def graph(type: str | None = None, min_edges: int = 0) -> dict:
    """Return full graph data for visualization."""
    if not is_initialized(DEFAULT_DB_PATH):
        raise HTTPException(status_code=503, detail="Database not initialized")

    conn = get_connection(DEFAULT_DB_PATH)
    try:
        nodes_sql = "SELECT id, type, name, properties, confidence FROM nodes"
        if type:
            nodes_sql += f" WHERE type = '{type}'"
        nodes = conn.execute(nodes_sql).fetchall()

        edges = conn.execute(
            "SELECT id, source_id, target_id, type, confidence FROM edges"
        ).fetchall()

        node_list = [
            {
                "id": n[0],
                "type": n[1],
                "name": n[2],
                "properties": json.loads(n[3]) if n[3] else {},
                "confidence": n[4],
            }
            for n in nodes
        ]

        if min_edges > 0:
            edge_counts: dict[str, int] = {}
            for e in edges:
                edge_counts[e[1]] = edge_counts.get(e[1], 0) + 1
                edge_counts[e[2]] = edge_counts.get(e[2], 0) + 1
            node_list = [n for n in node_list if edge_counts.get(n["id"], 0) >= min_edges]

        node_ids = {n["id"] for n in node_list}
        link_list = [
            {"id": e[0], "source": e[1], "target": e[2], "type": e[3], "confidence": e[4]}
            for e in edges
            if e[1] in node_ids and e[2] in node_ids
        ]

        return {"nodes": node_list, "links": link_list}
    finally:
        conn.close()


@app.get("/api/graph/stats")
def graph_stats() -> dict:
    """Graph statistics for the sidebar."""
    if not is_initialized(DEFAULT_DB_PATH):
        raise HTTPException(status_code=503, detail="Database not initialized")

    conn = get_connection(DEFAULT_DB_PATH)
    try:
        nodes_by_type = conn.execute(
            "SELECT type, COUNT(*) as count FROM nodes GROUP BY type ORDER BY count DESC"
        ).fetchall()
        edges_by_type = conn.execute(
            "SELECT type, COUNT(*) as count FROM edges GROUP BY type ORDER BY count DESC"
        ).fetchall()
        totals = {
            "nodes": (conn.execute("SELECT COUNT(*) FROM nodes").fetchone() or (0,))[0],
            "edges": (conn.execute("SELECT COUNT(*) FROM edges").fetchone() or (0,))[0],
            "artifacts": (conn.execute("SELECT COUNT(*) FROM artifacts").fetchone() or (0,))[0],
            "chunks": (conn.execute("SELECT COUNT(*) FROM chunks").fetchone() or (0,))[0],
        }
        return {
            "totals": totals,
            "nodesByType": [{"type": r[0], "count": r[1]} for r in nodes_by_type],
            "edgesByType": [{"type": r[0], "count": r[1]} for r in edges_by_type],
        }
    finally:
        conn.close()


@app.get("/api/graph/node/{node_id}")
def graph_node(node_id: str) -> dict:
    """Get node details with its connections."""
    if not is_initialized(DEFAULT_DB_PATH):
        raise HTTPException(status_code=503, detail="Database not initialized")

    conn = get_connection(DEFAULT_DB_PATH)
    try:
        row = conn.execute(
            "SELECT id, type, name, properties, confidence FROM nodes WHERE id = ?", [node_id]
        ).fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Node not found")

        out_edges = conn.execute(
            "SELECT e.id, e.type, e.target_id, n.name, n.type "
            "FROM edges e JOIN nodes n ON e.target_id = n.id WHERE e.source_id = ?",
            [node_id],
        ).fetchall()

        in_edges = conn.execute(
            "SELECT e.id, e.type, e.source_id, n.name, n.type "
            "FROM edges e JOIN nodes n ON e.source_id = n.id WHERE e.target_id = ?",
            [node_id],
        ).fetchall()

        return {
            "id": row[0],
            "type": row[1],
            "name": row[2],
            "properties": json.loads(row[3]) if row[3] else {},
            "confidence": row[4],
            "outEdges": [
                {"id": e[0], "type": e[1], "targetId": e[2], "targetName": e[3], "targetType": e[4]}
                for e in out_edges
            ],
            "inEdges": [
                {"id": e[0], "type": e[1], "sourceId": e[2], "sourceName": e[3], "sourceType": e[4]}
                for e in in_edges
            ],
        }
    finally:
        conn.close()


@app.get("/api/graph/search")
def graph_search(q: str = "") -> list[dict]:
    """Search nodes by name."""
    if not q:
        return []

    conn = get_connection(DEFAULT_DB_PATH)
    try:
        results = conn.execute(
            "SELECT id, type, name FROM nodes WHERE LOWER(name) LIKE ? LIMIT 20",
            [f"%{q.lower()}%"],
        ).fetchall()
        return [{"id": r[0], "type": r[1], "name": r[2]} for r in results]
    finally:
        conn.close()


@app.get("/api/timeline")
def timeline() -> dict:
    """Return time-bucketed artifact data for timeline visualization."""
    if not is_initialized(DEFAULT_DB_PATH):
        raise HTTPException(status_code=503, detail="Database not initialized")

    conn = get_connection(DEFAULT_DB_PATH)
    try:
        artifacts = conn.execute("""
            SELECT id, file_name, file_type, classification, ingested_at,
                   SUBSTRING(raw_text, 1, 200) as snippet
            FROM artifacts
            WHERE classification IS NOT NULL
        """).fetchall()

        timeline_items = []
        for art in artifacts:
            art_id, file_name, file_type, classification_json, ingested_at, snippet = art
            classification = json.loads(classification_json) if classification_json else {}
            dates = classification.get("dates", [])
            art_type = classification.get("type", "other")
            claims = classification.get("claims", [])
            skills = classification.get("skills", [])
            projects = classification.get("projects", [])
            orgs = classification.get("organizations", [])

            date_str = dates[0]["date"] if dates else None

            timeline_items.append(
                {
                    "id": art_id,
                    "fileName": file_name,
                    "fileType": file_type,
                    "type": art_type,
                    "date": date_str,
                    "claims": claims[:3],
                    "skills": skills[:5],
                    "projects": projects[:3],
                    "organizations": [o.get("name", "") for o in orgs]
                    if isinstance(orgs, list)
                    else [],
                    "snippet": snippet.strip() if snippet else "",
                }
            )

        # Bucket by year-month for heatmap
        heatmap: dict[str, int] = {}
        for item in timeline_items:
            if item["date"]:
                ym = item["date"][:7]  # YYYY-MM
                heatmap[ym] = heatmap.get(ym, 0) + 1

        # Career periods
        career = [
            {"org": "IBM", "start": "2007-07", "end": "2013-03", "role": "Software Engineer"},
            {
                "org": "Exeter Group / OneGate",
                "start": "2013-03",
                "end": "2016-02",
                "role": "Senior Tech Lead",
            },
            {
                "org": "Amazon",
                "start": "2016-02",
                "end": "2018-08",
                "role": "Software Development Engineer",
            },
            {"org": "Philips India", "start": "2018-09", "end": "2021-11", "role": "Principal TPM"},
            {
                "org": "Philips North America",
                "start": "2021-11",
                "end": "2026-07",
                "role": "Principal TPM",
            },
        ]

        # Category lanes
        categories: dict[str, list[dict]] = {
            "Employment": [],
            "Teaching & Talks": [],
            "Awards & Recognition": [],
            "Education & Certification": [],
            "Community": [],
        }
        for item in timeline_items:
            if not item["date"]:
                continue
            t = item["type"]
            if t == "performance_review":
                categories["Employment"].append(item)
            elif t == "presentation":
                categories["Teaching & Talks"].append(item)
            elif t in ("email_appreciation", "recommendation"):
                categories["Awards & Recognition"].append(item)
            elif t == "certificate":
                categories["Education & Certification"].append(item)
            elif t == "other" and any(
                s in item["fileName"].lower() for s in ["yoga", "volunteer", "community"]
            ):
                categories["Community"].append(item)
            elif t == "other" and any(
                s in item["fileName"].lower()
                for s in ["talk", "seminar", "workshop", "presentation"]
            ):
                categories["Teaching & Talks"].append(item)
            else:
                categories["Employment"].append(item)

        return {
            "items": timeline_items,
            "heatmap": heatmap,
            "career": career,
            "categories": {k: v for k, v in categories.items()},
        }
    finally:
        conn.close()


def _estimate_confidence(evidence: list[dict]) -> float:
    """Estimate answer confidence based on evidence quality."""
    if not evidence:
        return 0.1
    avg_score = sum(e.get("score", 0) for e in evidence) / len(evidence)
    count_factor = min(len(evidence) / 5.0, 1.0)
    return min(avg_score * count_factor * 5, 1.0)
