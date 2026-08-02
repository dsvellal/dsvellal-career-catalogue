"""Watch folder: monitor a local directory for new files and auto-ingest."""

from pathlib import Path

import duckdb

from twin.ingestion.pipeline import ingest_file

DEFAULT_INBOX = Path.home() / "twin-inbox"


def watch_once(
    conn: duckdb.DuckDBPyConnection,
    inbox: Path = DEFAULT_INBOX,
) -> int:
    """Scan inbox for new files and ingest them. Returns count ingested."""
    if not inbox.exists():
        return 0

    ingested = 0
    for path in inbox.iterdir():
        if path.is_file() and not path.name.startswith("."):
            result = ingest_file(path, conn, channel="watch")
            if result.status == "processed":
                ingested += 1
                path.rename(inbox / ".processed" / path.name)
            elif result.status == "skipped":
                path.rename(inbox / ".processed" / path.name)

    return ingested


def setup_inbox(inbox: Path = DEFAULT_INBOX) -> Path:
    """Create the inbox directory and processed subfolder."""
    inbox.mkdir(parents=True, exist_ok=True)
    (inbox / ".processed").mkdir(exist_ok=True)
    return inbox
