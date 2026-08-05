"""End-to-end ingestion pipeline: extract, dedup, classify, resolve, link, log."""

import hashlib
import json
import uuid
from dataclasses import dataclass
from pathlib import Path

import duckdb

from twin.ingestion.classifier import ClassificationResult, classify
from twin.ingestion.edges import create_edges
from twin.ingestion.extractors import ExtractionResult, extract
from twin.ingestion.resolver import resolve
from twin.media import store_media
from twin.retrieval.chunker import chunk_text, store_chunks


@dataclass
class IngestResult:
    artifact_id: str
    status: str
    file_name: str
    file_type: str
    nodes_created: int = 0
    nodes_matched: int = 0
    edges_created: int = 0
    skipped_reason: str = ""


def ingest_file(
    path: Path,
    conn: duckdb.DuckDBPyConnection,
    context: str = "",
    channel: str = "cli",
    api_key: str | None = None,
    media_url: str = "",
) -> IngestResult:
    """Run the full ingestion pipeline on a single file."""
    path = path.resolve()
    if not path.exists():
        return IngestResult(
            artifact_id="",
            status="failed",
            file_name=path.name,
            file_type="",
            skipped_reason=f"File not found: {path}",
        )

    extraction = extract(path)

    content_hash = hashlib.sha256(extraction.text.encode()).hexdigest()
    existing = conn.execute(
        "SELECT id FROM artifacts WHERE content_hash = ?", [content_hash]
    ).fetchone()
    if existing:
        return IngestResult(
            artifact_id=existing[0],
            status="skipped",
            file_name=path.name,
            file_type=extraction.file_type,
            skipped_reason="Duplicate content",
        )

    artifact_id = f"art_{uuid.uuid4().hex[:12]}"

    classification = _classify_safe(extraction, api_key)

    resolution = resolve(classification, conn)

    edges_created = create_edges(resolution, classification, artifact_id, conn)

    media_path = store_media(path, content_hash)

    metadata = extraction.metadata.copy()
    if context:
        metadata["user_context"] = context

    conn.execute(
        "INSERT INTO artifacts (id, file_path, file_name, file_type, content_hash, "
        "source_channel, status, metadata, classification, raw_text, media_path, media_url) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [
            artifact_id,
            str(path),
            path.name,
            extraction.file_type,
            content_hash,
            channel,
            "processed",
            json.dumps(metadata),
            json.dumps(_classification_to_dict(classification)),
            extraction.text,
            media_path,
            media_url or None,
        ],
    )

    chunks = chunk_text(extraction.text, artifact_id)
    store_chunks(chunks, conn)

    _log_action(
        conn,
        "ingest",
        artifact_id,
        channel,
        {
            "file": path.name,
            "nodes_created": len(resolution.nodes_created),
            "nodes_matched": len(resolution.nodes_matched),
            "edges_created": edges_created,
        },
    )

    return IngestResult(
        artifact_id=artifact_id,
        status="processed",
        file_name=path.name,
        file_type=extraction.file_type,
        nodes_created=len(resolution.nodes_created),
        nodes_matched=len(resolution.nodes_matched),
        edges_created=edges_created,
    )


def ingest_pre_classified(
    classification_data: dict,
    conn: duckdb.DuckDBPyConnection,
    file_name: str = "unknown",
    file_type: str = "image",
    raw_text: str = "",
    media_url: str = "",
    context: str = "",
    channel: str = "cli",
) -> IngestResult:
    """Ingest with a pre-computed classification (no LLM call needed).

    Use when classification is generated externally (e.g., by Claude in an interactive session).
    """
    content_hash = hashlib.sha256((raw_text or media_url or file_name).encode()).hexdigest()

    existing = conn.execute(
        "SELECT id FROM artifacts WHERE content_hash = ?", [content_hash]
    ).fetchone()
    if existing:
        return IngestResult(
            artifact_id=existing[0],
            status="skipped",
            file_name=file_name,
            file_type=file_type,
            skipped_reason="Duplicate content",
        )

    artifact_id = f"art_{uuid.uuid4().hex[:12]}"

    classification = ClassificationResult(
        type=classification_data.get("type", "other"),
        dates=classification_data.get("dates", []),
        projects=classification_data.get("projects", []),
        skills=classification_data.get("skills", []),
        people=classification_data.get("people", []),
        organizations=classification_data.get("organizations", []),
        claims=classification_data.get("claims", []),
        confidence=classification_data.get("confidence", 0.9),
    )

    resolution = resolve(classification, conn)
    edges_created = create_edges(resolution, classification, artifact_id, conn)

    metadata = {}
    if context:
        metadata["user_context"] = context

    conn.execute(
        "INSERT INTO artifacts (id, file_path, file_name, file_type, content_hash, "
        "source_channel, status, metadata, classification, raw_text, media_path, media_url) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [
            artifact_id,
            None,
            file_name,
            file_type,
            content_hash,
            channel,
            "processed",
            json.dumps(metadata),
            json.dumps(classification_data),
            raw_text,
            None,
            media_url or None,
        ],
    )

    _log_action(
        conn,
        "ingest",
        artifact_id,
        channel,
        {
            "file": file_name,
            "nodes_created": len(resolution.nodes_created),
            "nodes_matched": len(resolution.nodes_matched),
            "edges_created": edges_created,
            "source": "pre_classified",
        },
    )

    return IngestResult(
        artifact_id=artifact_id,
        status="processed",
        file_name=file_name,
        file_type=file_type,
        nodes_created=len(resolution.nodes_created),
        nodes_matched=len(resolution.nodes_matched),
        edges_created=edges_created,
    )


def _classify_safe(extraction: ExtractionResult, api_key: str | None) -> ClassificationResult:
    """Classify using Gemini if available, otherwise use local rule-based extraction."""
    if not api_key:
        import os

        api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        try:
            return classify(extraction.text, extraction.file_type, api_key=api_key)
        except Exception:
            pass

    return _classify_local(extraction)


def _classify_local(extraction: ExtractionResult) -> ClassificationResult:
    """Rule-based classification using structured metadata and content patterns."""
    from scripts.enrich_emails import (
        classify_email_type,
        extract_claims,
        extract_dates,
        extract_people_from_email,
        extract_projects_from_text,
        extract_skills_from_text,
    )

    metadata = extraction.metadata
    subject = metadata.get("subject", "")
    text = extraction.text

    return ClassificationResult(
        type=classify_email_type(subject, text, metadata),
        dates=extract_dates(metadata),
        projects=extract_projects_from_text(text),
        skills=extract_skills_from_text(text),
        people=extract_people_from_email(metadata, text),
        organizations=[{"name": "Philips", "role": "employer"}]
        if "philips" in text.lower()
        else [],
        claims=extract_claims(text, subject, metadata),
        confidence=0.85,
    )


def _classification_to_dict(c: ClassificationResult) -> dict:
    return {
        "type": c.type,
        "dates": c.dates,
        "projects": c.projects,
        "skills": c.skills,
        "people": c.people,
        "organizations": c.organizations,
        "claims": c.claims,
        "confidence": c.confidence,
    }


def _log_action(
    conn: duckdb.DuckDBPyConnection,
    action: str,
    artifact_id: str,
    channel: str,
    details: dict,
) -> None:
    log_id = f"log_{uuid.uuid4().hex[:12]}"
    conn.execute(
        "INSERT INTO ingestion_log (id, action, artifact_id, channel, details) "
        "VALUES (?, ?, ?, ?, ?)",
        [log_id, action, artifact_id, channel, json.dumps(details)],
    )
