"""Semantic chunking: split text into meaningful segments for embedding."""

import re
import uuid
from dataclasses import dataclass

import duckdb


@dataclass
class Chunk:
    id: str
    artifact_id: str
    sequence: int
    content: str
    section: str = ""


DEFAULT_CHUNK_SIZE = 512
DEFAULT_OVERLAP = 64


def chunk_text(
    text: str,
    artifact_id: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_OVERLAP,
) -> list[Chunk]:
    """Split text into chunks using section-aware semantic boundaries."""
    if not text.strip():
        return []

    sections = _split_into_sections(text)
    chunks: list[Chunk] = []
    seq = 0

    for section_title, section_text in sections:
        paragraphs = _split_into_paragraphs(section_text, chunk_size)
        current = ""

        for para in paragraphs:
            if len(current) + len(para) + 1 > chunk_size and current:
                chunks.append(_make_chunk(current, artifact_id, seq, section_title))
                seq += 1
                # Keep overlap from end of current chunk
                if overlap > 0 and len(current) > overlap:
                    current = current[-overlap:] + "\n\n" + para
                else:
                    current = para
            else:
                current = current + "\n\n" + para if current else para

        if current.strip():
            chunks.append(_make_chunk(current, artifact_id, seq, section_title))
            seq += 1

    return chunks


def store_chunks(chunks: list[Chunk], conn: duckdb.DuckDBPyConnection) -> int:
    """Store chunks in the database. Returns count stored."""
    for chunk in chunks:
        conn.execute(
            "INSERT INTO chunks (id, artifact_id, sequence, content, section) "
            "VALUES (?, ?, ?, ?, ?)",
            [chunk.id, chunk.artifact_id, chunk.sequence, chunk.content, chunk.section],
        )
    conn.execute(
        "UPDATE artifacts SET chunk_count = ? WHERE id = ?",
        [len(chunks), chunks[0].artifact_id] if chunks else [0, ""],
    )
    return len(chunks)


def _split_into_sections(text: str) -> list[tuple[str, str]]:
    """Split text by markdown headers or logical sections."""
    header_pattern = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)
    matches = list(header_pattern.finditer(text))

    if not matches:
        return [("", text)]

    sections = []
    for i, match in enumerate(matches):
        title = match.group(2).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[start:end].strip()
        if content:
            sections.append((title, content))

    # Include any text before the first header
    pre_header = text[: matches[0].start()].strip()
    if pre_header:
        sections.insert(0, ("", pre_header))

    return sections


def _split_into_paragraphs(text: str, max_len: int = DEFAULT_CHUNK_SIZE) -> list[str]:
    """Split text into paragraphs, breaking long ones at sentence boundaries."""
    raw_paragraphs = re.split(r"\n\s*\n", text)
    result = []
    for para in raw_paragraphs:
        para = para.strip()
        if not para:
            continue
        if len(para) <= max_len:
            result.append(para)
        else:
            result.extend(_split_long_paragraph(para, max_len))
    return result


def _split_long_paragraph(text: str, max_len: int) -> list[str]:
    """Break a long paragraph at sentence boundaries."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks = []
    current = ""
    for sentence in sentences:
        if len(current) + len(sentence) + 1 > max_len and current:
            chunks.append(current)
            current = sentence
        else:
            current = current + " " + sentence if current else sentence
    if current:
        chunks.append(current)
    return chunks


def _make_chunk(content: str, artifact_id: str, seq: int, section: str) -> Chunk:
    return Chunk(
        id=f"chunk_{uuid.uuid4().hex[:12]}",
        artifact_id=artifact_id,
        sequence=seq,
        content=content.strip(),
        section=section,
    )
