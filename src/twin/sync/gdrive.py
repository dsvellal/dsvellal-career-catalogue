"""Google Drive sync: detect changes and trigger ingestion."""

import uuid
from dataclasses import dataclass, field
from pathlib import Path

import duckdb


@dataclass
class DriveChange:
    file_id: str
    name: str
    action: str  # new|modified|deleted|moved
    mime_type: str = ""


@dataclass
class SyncResult:
    changes_detected: int = 0
    files_ingested: int = 0
    files_deleted: int = 0
    errors: list[str] = field(default_factory=list)


class GoogleDriveSync:
    """Manages Google Drive sync state and change detection."""

    def __init__(
        self,
        credentials_path: Path,
        conn: duckdb.DuckDBPyConnection,
        download_dir: Path = Path("./data/gdrive_downloads"),
    ):
        self.credentials_path = credentials_path
        self.conn = conn
        self.download_dir = download_dir
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self._token: str | None = None

    def get_page_token(self) -> str | None:
        """Get stored page token for incremental sync."""
        row = self.conn.execute(
            "SELECT page_token FROM gdrive_sync WHERE drive_file_id = '__page_token__'"
        ).fetchone()
        return row[0] if row else None

    def store_page_token(self, token: str) -> None:
        """Store page token after successful sync."""
        existing = self.conn.execute(
            "SELECT id FROM gdrive_sync WHERE drive_file_id = '__page_token__'"
        ).fetchone()
        if existing:
            self.conn.execute(
                "UPDATE gdrive_sync SET page_token = ?, last_synced_at = CURRENT_TIMESTAMP "
                "WHERE drive_file_id = '__page_token__'",
                [token],
            )
        else:
            row_id = f"sync_{uuid.uuid4().hex[:8]}"
            self.conn.execute(
                "INSERT INTO gdrive_sync (id, drive_file_id, drive_name, page_token, "
                "sync_status, last_synced_at) "
                "VALUES (?, '__page_token__', '__page_token__', ?, 'synced', CURRENT_TIMESTAMP)",
                [row_id, token],
            )

    def detect_changes(self, page_token: str | None = None) -> tuple[list[DriveChange], str]:
        """Detect changes since last sync. Returns (changes, new_page_token).

        This is the interface — actual Drive API calls are delegated to _fetch_changes.
        """
        token = page_token or self.get_page_token()
        if not token:
            token = self._get_start_page_token()

        changes, new_token = self._fetch_changes(token)
        return changes, new_token

    def process_change(self, change: DriveChange) -> str:
        """Process a single change. Returns status: ingested|deleted|skipped|error."""
        if change.action == "deleted":
            return self._handle_delete(change)
        elif change.action in ("new", "modified"):
            return self._handle_new_or_modified(change)
        return "skipped"

    def sync(self) -> SyncResult:
        """Run a full sync cycle: detect changes, process each."""
        result = SyncResult()
        try:
            changes, new_token = self.detect_changes()
            result.changes_detected = len(changes)

            for change in changes:
                try:
                    status = self.process_change(change)
                    if status == "ingested":
                        result.files_ingested += 1
                    elif status == "deleted":
                        result.files_deleted += 1
                except Exception as e:
                    result.errors.append(f"{change.name}: {e}")

            self.store_page_token(new_token)
        except Exception as e:
            result.errors.append(f"Sync failed: {e}")

        return result

    def _get_start_page_token(self) -> str:
        """Get initial page token from Drive API."""
        return "1"

    def _fetch_changes(self, token: str) -> tuple[list[DriveChange], str]:
        """Fetch changes from Drive API. Override for testing."""
        raise NotImplementedError("Requires OAuth2 credentials and Drive API access")

    def _handle_delete(self, change: DriveChange) -> str:
        """Mark artifact as deleted (soft delete)."""
        row = self.conn.execute(
            "SELECT local_artifact_id FROM gdrive_sync WHERE drive_file_id = ?",
            [change.file_id],
        ).fetchone()
        if row and row[0]:
            artifact_id = row[0]
            self.conn.execute(
                "UPDATE gdrive_sync SET sync_status = 'deleted', local_artifact_id = NULL "
                "WHERE drive_file_id = ?",
                [change.file_id],
            )
            self.conn.execute("UPDATE artifacts SET status = 'deleted' WHERE id = ?", [artifact_id])
        return "deleted"

    def _handle_new_or_modified(self, change: DriveChange) -> str:
        """Download and ingest new/modified file."""
        download_path = self.download_dir / change.name
        self._download_file(change.file_id, download_path)

        from twin.ingestion.pipeline import ingest_file

        result = ingest_file(download_path, self.conn, channel="gdrive")

        existing = self.conn.execute(
            "SELECT id FROM gdrive_sync WHERE drive_file_id = ?", [change.file_id]
        ).fetchone()
        if existing:
            self.conn.execute(
                "UPDATE gdrive_sync SET drive_name = ?, local_artifact_id = ?, "
                "sync_status = 'synced', last_synced_at = CURRENT_TIMESTAMP "
                "WHERE drive_file_id = ?",
                [change.name, result.artifact_id, change.file_id],
            )
        else:
            sync_id = f"sync_{uuid.uuid4().hex[:8]}"
            self.conn.execute(
                "INSERT INTO gdrive_sync (id, drive_file_id, drive_name, "
                "local_artifact_id, sync_status, last_synced_at) "
                "VALUES (?, ?, ?, ?, 'synced', CURRENT_TIMESTAMP)",
                [sync_id, change.file_id, change.name, result.artifact_id],
            )
        return "ingested" if result.status == "processed" else "skipped"

    def _download_file(self, file_id: str, dest: Path) -> None:
        """Download file from Drive. Override for testing."""
        raise NotImplementedError("Requires OAuth2 credentials")
