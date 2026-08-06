"""Evidence index builder — parses evidence markdown files and indexes them in DuckDB.

Scans data/evidence/<year>/individual/*.md files, extracts structured metadata,
and maintains a queryable evidence_index table for the visualization layer.
"""

from __future__ import annotations

import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Any

import duckdb

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

EVIDENCE_INDEX_SQL = """
CREATE TABLE IF NOT EXISTS evidence_index (
    id VARCHAR PRIMARY KEY,
    file_path VARCHAR NOT NULL,
    file_name VARCHAR NOT NULL,
    title VARCHAR,
    year INTEGER,
    date VARCHAR,
    era VARCHAR,
    category VARCHAR,
    channel VARCHAR,
    involvement_type VARCHAR,
    role_at_time VARCHAR,
    people VARCHAR[],
    skills VARCHAR[],
    programs VARCHAR[],
    quotes VARCHAR[],
    nps_score FLOAT,
    metric_value VARCHAR,
    metric_label VARCHAR,
    source_type VARCHAR,
    has_image BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

EVIDENCE_INDEX_INDEXES_SQL = """
CREATE INDEX IF NOT EXISTS idx_evidence_year ON evidence_index(year);
CREATE INDEX IF NOT EXISTS idx_evidence_era ON evidence_index(era);
CREATE INDEX IF NOT EXISTS idx_evidence_category ON evidence_index(category);
CREATE INDEX IF NOT EXISTS idx_evidence_channel ON evidence_index(channel);
"""


def create_evidence_index_table(conn: duckdb.DuckDBPyConnection) -> None:
    """Create the evidence_index table and indexes if they do not exist."""
    conn.execute(EVIDENCE_INDEX_SQL)
    conn.execute(EVIDENCE_INDEX_INDEXES_SQL)


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

_RE_TITLE = re.compile(r"^#\s+Evidence:\s*(.+)", re.MULTILINE)
_RE_DATE = re.compile(r"\*\*Date:\*\*\s*(.+)")
_RE_CATEGORY = re.compile(r"\*\*Category:\*\*\s*(.+)")
_RE_CHANNEL = re.compile(r"\*\*Channel:\*\*\s*(.+)")
_RE_ROLE = re.compile(r"\*\*Role at time:\*\*\s*(.+)")
_RE_INVOLVEMENT = re.compile(r"\*\*Involvement type:\*\*\s*(.+)")
_RE_PROGRAM = re.compile(r"\*\*Program referenced:\*\*\s*(.+)")
_RE_FROM = re.compile(r"\*\*From:\*\*\s*(.+)")
_RE_TO = re.compile(r"\*\*To:\*\*\s*(.+)")
_RE_CC = re.compile(r"\*\*CC:\*\*\s*(.+)")
_RE_PEOPLE_VISIBLE = re.compile(r"\*\*People visible:\*\*\s*(.+)")
_RE_FILE = re.compile(r"\*\*File:\*\*\s*`?([^`\n]+)`?")
_RE_PLATFORM = re.compile(r"\*\*Platform:\*\*\s*(.+)")

# NPS patterns: "NPS 92.9", "NPS: 8.9", "NPS +79", "NPS from 29 sessions: 8.9",
# "9.75/10", "8.9/10", "NPS - 10"
_RE_NPS_EXPLICIT = re.compile(r"NPS[:\s\-]+\+?(\d+\.?\d*)", re.IGNORECASE)
_RE_NPS_FROM = re.compile(r"NPS\s+from\s+\d+\s+sessions[:\s]+(\d+\.?\d*)", re.IGNORECASE)
_RE_NPS_SCORE_SLASH = re.compile(r"(\d+\.?\d*)\s*/\s*10")

# Image references
_RE_IMAGE_REF = re.compile(r"\.(jpg|jpeg|png|gif|webp|svg)", re.IGNORECASE)

# Person name extraction from email headers
_RE_PERSON_NAME = re.compile(
    r'"?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*),\s*([A-Z][a-z]+(?:\s*\([^)]*\))?)"?'
)
_RE_PERSON_SIMPLE = re.compile(r"([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)")


def _extract_first(pattern: re.Pattern[str], text: str) -> str | None:
    """Extract first match of a pattern, returning the first group or None."""
    m = pattern.search(text)
    return m.group(1).strip() if m else None


def _extract_people(text: str) -> list[str]:
    """Extract unique people names from email metadata fields."""
    people: set[str] = set()

    # Extract from From/To/CC fields
    for pattern in (_RE_FROM, _RE_TO, _RE_CC, _RE_PEOPLE_VISIBLE):
        match = pattern.search(text)
        if match:
            field_text = match.group(1)
            # Match "Last, First" patterns
            for m in _RE_PERSON_NAME.finditer(field_text):
                last_name = m.group(1).strip()
                first_name = m.group(2).strip().split("(")[0].strip()
                people.add(f"{first_name} {last_name}")

    # Remove Datta's own name variants
    datta_variants = {
        "Dattatreya Subramanya Vellal",
        "Subramanya Vellal Dattatreya",
        "Dattatreya Vellal",
        "Datta Vellal",
    }
    people -= datta_variants

    return sorted(people) if people else []


def _extract_quotes(text: str) -> list[str]:
    """Extract blockquote lines from the Key Quotes section."""
    quotes: list[str] = []
    in_key_quotes = False

    for line in text.splitlines():
        stripped = line.strip()

        # Detect entering/leaving Key Quotes section
        if stripped.startswith("## Key Quotes"):
            in_key_quotes = True
            continue
        if in_key_quotes and stripped.startswith("## "):
            break

        if in_key_quotes and stripped.startswith(">"):
            quote_text = stripped.lstrip("> ").strip()
            # Skip trivially short or metadata-like quotes
            if len(quote_text) > 20 and not quote_text.startswith("Subject:"):
                quotes.append(quote_text)

    return quotes


def _extract_skills(text: str) -> list[str]:
    """Extract skills from a Skills Demonstrated section if present."""
    skills: list[str] = []
    in_skills = False

    for line in text.splitlines():
        stripped = line.strip()

        if "Skills Demonstrated" in stripped or "## Skills" in stripped:
            in_skills = True
            continue
        if in_skills and stripped.startswith("## "):
            break
        if in_skills and stripped.startswith("- "):
            skill = stripped.lstrip("- ").strip()
            if skill:
                skills.append(skill)

    return skills


def _extract_nps_score(text: str) -> float | None:
    """Extract NPS score from content using various patterns."""
    # Try "NPS from N sessions: X" pattern first (most specific)
    m = _RE_NPS_FROM.search(text)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            pass

    # Try explicit NPS patterns
    m = _RE_NPS_EXPLICIT.search(text)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            pass

    # Try X/10 pattern (satisfaction scores)
    matches = _RE_NPS_SCORE_SLASH.findall(text)
    if matches:
        # Return the first valid score
        for score_str in matches:
            try:
                score = float(score_str)
                if 0 <= score <= 10:
                    return score
            except ValueError:
                continue

    return None


def _determine_era(year: int | None, date_str: str | None, content: str) -> str:
    """Determine the era based on year, date, and content context."""
    if year is None:
        return "Independent"

    # Check for Amazon references in early years
    if year in (2017, 2018) and "amazon" in content.lower():
        return "Amazon"

    # IBM era
    if 2007 <= year <= 2014:
        return "IBM"

    # Exeter era
    if 2014 < year <= 2017:
        return "Exeter"

    # Philips split: India vs USA
    if 2018 <= year <= 2021:
        # Check if date is after Dec 5, 2021 (unlikely for 2018-2020 but handle 2021)
        if year == 2021 and date_str:
            try:
                # Try parsing various date formats
                for fmt in ("%Y-%m-%d", "%d %b %Y", "%B %d, %Y"):
                    try:
                        dt = datetime.strptime(date_str.strip()[:10], fmt)
                        if dt.month == 12 and dt.day >= 5:
                            return "Philips USA"
                        break
                    except ValueError:
                        continue
            except Exception:
                pass
        return "Philips India"

    if year >= 2022:
        return "Philips USA"

    return "Independent"


def _extract_year_from_path(file_path: Path) -> int | None:
    """Extract the year from the file path (e.g., data/evidence/2020/individual/...)."""
    for part in file_path.parts:
        if part.isdigit() and len(part) == 4:
            year = int(part)
            if 2000 <= year <= 2100:
                return year
    return None


def _generate_id(file_path: Path) -> str:
    """Generate a stable ID from the file path relative to evidence dir."""
    # Use the year + filename stem as a stable ID
    stem = file_path.stem
    year = _extract_year_from_path(file_path)
    if year:
        return f"{year}/{stem}"
    return stem


def _extract_source_type(text: str, file_path: Path) -> str | None:
    """Determine the source artifact type."""
    file_field = _extract_first(_RE_FILE, text)
    platform_field = _extract_first(_RE_PLATFORM, text)

    if platform_field:
        platform_lower = platform_field.lower()
        if "viva engage" in platform_lower:
            return "viva_engage"
        if "linkedin" in platform_lower:
            return "linkedin"
        if "teams" in platform_lower:
            return "teams"
        return "social_post"

    if file_field:
        file_lower = file_field.lower()
        if file_lower.endswith((".eml", ".msg")):
            return "email"
        if file_lower.endswith(".pdf"):
            return "pdf"
        if file_lower.endswith((".pptx", ".ppt")):
            return "presentation"
        if file_lower.endswith((".xlsx", ".xls", ".csv")):
            return "spreadsheet"
        if file_lower.endswith((".docx", ".doc")):
            return "document"
        if file_lower.endswith((".jpg", ".jpeg", ".png", ".gif")):
            return "image"

    # Check channel for hints
    channel = _extract_first(_RE_CHANNEL, text)
    if channel:
        channel_lower = channel.lower()
        if "email" in channel_lower:
            return "email"
        if "snapshot" in channel_lower:
            return "internal_snapshot"
        if "github" in channel_lower:
            return "github"

    return None


def _extract_metric(text: str) -> tuple[str | None, str | None]:
    """Extract a key metric value and label from the content.

    Returns (metric_value, metric_label) tuple.
    """
    # Look for common metric patterns
    patterns = [
        (r"(\d+\.?\d*)\s*%\s*(confidence increase)", "confidence_increase"),
        (r"(\d+)\s+sessions?\s+conducted", "sessions_conducted"),
        (r"(\d+)\s+learners?", "total_learners"),
        (r"(\d[\d,]*)\s+lines?\s+removed", "lines_removed"),
        (r"(\d+)\s+employees?", "employees_reached"),
        (r"(\d[\d,]*\.?\d*)\s*[Kk]\s*euros?", "budget_euros_k"),
        (r"Seen by:\*\*\s*(\d+)", "viva_engage_views"),
    ]

    for pattern, label in patterns:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            return m.group(1), label

    return None, None


# ---------------------------------------------------------------------------
# Main parse function
# ---------------------------------------------------------------------------


def parse_evidence_file(file_path: Path) -> dict[str, Any]:
    """Parse a single evidence markdown file and return structured metadata.

    Args:
        file_path: Absolute path to the evidence markdown file.

    Returns:
        Dictionary with fields matching the evidence_index table schema.

    Raises:
        FileNotFoundError: If the file does not exist.
        UnicodeDecodeError: If the file cannot be read as UTF-8.
    """
    content = file_path.read_text(encoding="utf-8")
    year = _extract_year_from_path(file_path)
    date_str = _extract_first(_RE_DATE, content)

    # Extract NPS
    nps_score = _extract_nps_score(content)

    # Extract metric
    metric_value, metric_label = _extract_metric(content)

    # Extract programs (may be comma-separated)
    programs_raw = _extract_first(_RE_PROGRAM, content)
    programs = [p.strip() for p in programs_raw.split(",") if p.strip()] if programs_raw else []

    result: dict[str, Any] = {
        "id": _generate_id(file_path),
        "file_path": str(file_path),
        "file_name": file_path.name,
        "title": _extract_first(_RE_TITLE, content),
        "year": year,
        "date": date_str,
        "era": _determine_era(year, date_str, content),
        "category": _extract_first(_RE_CATEGORY, content),
        "channel": _extract_first(_RE_CHANNEL, content),
        "involvement_type": _extract_first(_RE_INVOLVEMENT, content),
        "role_at_time": _extract_first(_RE_ROLE, content),
        "people": _extract_people(content),
        "skills": _extract_skills(content),
        "programs": programs,
        "quotes": _extract_quotes(content),
        "nps_score": nps_score,
        "metric_value": metric_value,
        "metric_label": metric_label,
        "source_type": _extract_source_type(content, file_path),
        "has_image": bool(_RE_IMAGE_REF.search(content)),
    }

    return result


# ---------------------------------------------------------------------------
# Index management
# ---------------------------------------------------------------------------


def rebuild_evidence_index(
    conn: duckdb.DuckDBPyConnection,
    evidence_dir: Path,
) -> dict[str, Any]:
    """Drop and rebuild the entire evidence index by scanning all evidence files.

    Args:
        conn: Active DuckDB connection.
        evidence_dir: Root evidence directory (e.g., data/evidence/).

    Returns:
        Stats dictionary with counts and any errors encountered.
    """
    stats: dict[str, Any] = {
        "total_files": 0,
        "indexed": 0,
        "skipped": 0,
        "errors": [],
        "by_year": {},
        "by_era": {},
        "by_category": {},
    }

    # Drop existing table and recreate
    conn.execute("DROP TABLE IF EXISTS evidence_index")
    create_evidence_index_table(conn)

    # Find all evidence markdown files in individual/ subdirectories
    evidence_files = sorted(evidence_dir.glob("**/individual/*.md"))

    # Filter out _INDEX.md files
    evidence_files = [f for f in evidence_files if not f.name.startswith("_")]

    stats["total_files"] = len(evidence_files)
    logger.info("Found %d evidence files to index", len(evidence_files))

    records: list[dict[str, Any]] = []

    for file_path in evidence_files:
        try:
            record = parse_evidence_file(file_path)
            records.append(record)
            stats["indexed"] += 1

            # Track stats by year
            year = record.get("year")
            if year:
                stats["by_year"][year] = stats["by_year"].get(year, 0) + 1

            # Track by era
            era = record.get("era") or "Unknown"
            stats["by_era"][era] = stats["by_era"].get(era, 0) + 1

            # Track by category
            category = record.get("category") or "Uncategorized"
            stats["by_category"][category] = stats["by_category"].get(category, 0) + 1

        except Exception as exc:
            stats["errors"].append({"file": str(file_path), "error": str(exc)})
            stats["skipped"] += 1
            logger.warning("Failed to parse %s: %s", file_path, exc)

    # Batch insert all records
    if records:
        _batch_insert(conn, records)

    logger.info(
        "Evidence index rebuilt: %d indexed, %d skipped, %d errors",
        stats["indexed"],
        stats["skipped"],
        len(stats["errors"]),
    )

    return stats


def _batch_insert(
    conn: duckdb.DuckDBPyConnection,
    records: list[dict[str, Any]],
) -> None:
    """Insert records into evidence_index using parameterized queries."""
    insert_sql = """
    INSERT INTO evidence_index (
        id, file_path, file_name, title, year, date, era, category, channel,
        involvement_type, role_at_time, people, skills, programs, quotes,
        nps_score, metric_value, metric_label, source_type, has_image
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    for record in records:
        try:
            conn.execute(
                insert_sql,
                [
                    record["id"],
                    record["file_path"],
                    record["file_name"],
                    record["title"],
                    record["year"],
                    record["date"],
                    record["era"],
                    record["category"],
                    record["channel"],
                    record["involvement_type"],
                    record["role_at_time"],
                    record["people"],
                    record["skills"],
                    record["programs"],
                    record["quotes"],
                    record["nps_score"],
                    record["metric_value"],
                    record["metric_label"],
                    record["source_type"],
                    record["has_image"],
                ],
            )
        except Exception as exc:
            logger.warning("Failed to insert record %s: %s", record["id"], exc)


# ---------------------------------------------------------------------------
# Query helper
# ---------------------------------------------------------------------------


def query_evidence(
    conn: duckdb.DuckDBPyConnection,
    *,
    era: str | None = None,
    year: int | None = None,
    category: str | None = None,
    channel: str | None = None,
    nps_gt: float | None = None,
    person: str | None = None,
    program: str | None = None,
    search: str | None = None,
    limit: int = 100,
    offset: int = 0,
) -> list[dict[str, Any]]:
    """Query the evidence index with optional keyword filters.

    Args:
        conn: Active DuckDB connection.
        era: Filter by era (e.g., "Philips India", "Philips USA").
        year: Filter by exact year.
        category: Filter by category (case-insensitive contains).
        channel: Filter by channel.
        nps_gt: Filter for NPS scores greater than this value.
        person: Filter for a person name present in the people array.
        program: Filter for a program name present in the programs array.
        search: Full-text search on title (case-insensitive contains).
        limit: Maximum number of results to return.
        offset: Number of results to skip.

    Returns:
        List of dictionaries with evidence record data.
    """
    conditions: list[str] = []
    params: list[Any] = []

    if era is not None:
        conditions.append("era = ?")
        params.append(era)

    if year is not None:
        conditions.append("year = ?")
        params.append(year)

    if category is not None:
        conditions.append("LOWER(category) LIKE ?")
        params.append(f"%{category.lower()}%")

    if channel is not None:
        conditions.append("channel = ?")
        params.append(channel)

    if nps_gt is not None:
        conditions.append("nps_score > ?")
        params.append(nps_gt)

    if person is not None:
        conditions.append("list_contains(people, ?)")
        params.append(person)

    if program is not None:
        conditions.append("list_contains(programs, ?)")
        params.append(program)

    if search is not None:
        conditions.append("LOWER(title) LIKE ?")
        params.append(f"%{search.lower()}%")

    where_clause = " WHERE " + " AND ".join(conditions) if conditions else ""
    sql = (  # noqa: S608
        f"SELECT * FROM evidence_index{where_clause} ORDER BY year DESC, date DESC LIMIT ? OFFSET ?"
    )
    params.extend([limit, offset])

    result = conn.execute(sql, params)
    columns = [desc[0] for desc in result.description]
    rows = result.fetchall()

    return [dict(zip(columns, row)) for row in rows]
