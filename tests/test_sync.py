"""Tests for Google Drive sync and watch folder."""

from pathlib import Path
from unittest.mock import patch

import pytest

from twin.db import get_connection, init_schema
from twin.sync.gdrive import DriveChange, GoogleDriveSync
from twin.sync.watcher import setup_inbox, watch_once


@pytest.fixture
def db(tmp_path: Path):
    db_path = tmp_path / "test.duckdb"
    init_schema(db_path)
    conn = get_connection(db_path)
    yield conn
    conn.close()


class TestGoogleDriveSync:
    def test_page_token_storage(self, db, tmp_path):
        sync = GoogleDriveSync(tmp_path / "creds.json", db)
        assert sync.get_page_token() is None
        sync.store_page_token("abc123")
        assert sync.get_page_token() == "abc123"

    def test_handle_delete(self, db, tmp_path):
        db.execute(
            "INSERT INTO artifacts (id, file_name, file_type, content_hash, "
            "source_channel, status) VALUES "
            "('art_1', 'file.md', 'md', 'h1', 'gdrive', 'processed')"
        )
        db.execute(
            "INSERT INTO gdrive_sync (id, drive_file_id, drive_name, "
            "local_artifact_id, sync_status) VALUES "
            "('s1', 'drive_123', 'file.md', 'art_1', 'synced')"
        )
        sync = GoogleDriveSync(tmp_path / "creds.json", db)
        change = DriveChange(file_id="drive_123", name="file.md", action="deleted")
        status = sync.process_change(change)
        assert status == "deleted"
        row = db.execute("SELECT status FROM artifacts WHERE id = 'art_1'").fetchone()
        assert row[0] == "deleted"

    def test_handle_new_file(self, db, tmp_path):
        sync = GoogleDriveSync(tmp_path / "creds.json", db, download_dir=tmp_path / "dl")

        # Mock download to create a file
        def _mock_download(file_id, dest):
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text("New content from Drive")

        sync._download_file = _mock_download

        change = DriveChange(file_id="drive_456", name="new.md", action="new")
        with patch.dict("os.environ", {}, clear=True):
            status = sync.process_change(change)
        assert status == "ingested"

    def test_sync_full_cycle(self, db, tmp_path):
        sync = GoogleDriveSync(tmp_path / "creds.json", db, download_dir=tmp_path / "dl")

        def _mock_fetch(token):
            return [
                DriveChange(file_id="d1", name="a.md", action="new"),
            ], "new_token"

        def _mock_download(file_id, dest):
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(f"Content for {file_id}")

        sync._fetch_changes = _mock_fetch
        sync._download_file = _mock_download
        sync.store_page_token("old_token")

        with patch.dict("os.environ", {}, clear=True):
            result = sync.sync()

        assert result.changes_detected == 1
        assert result.files_ingested == 1
        assert result.errors == []

    def test_sync_handles_errors(self, db, tmp_path):
        sync = GoogleDriveSync(tmp_path / "creds.json", db)

        def _mock_fetch(token):
            return [
                DriveChange(file_id="d1", name="bad.md", action="new"),
            ], "new_token"

        sync._fetch_changes = _mock_fetch
        sync.store_page_token("old_token")
        # _download_file raises NotImplementedError
        result = sync.sync()
        assert len(result.errors) >= 1
        assert "bad.md" in result.errors[0]


class TestWatchFolder:
    def test_setup_inbox(self, tmp_path):
        inbox = tmp_path / "inbox"
        result = setup_inbox(inbox)
        assert result.exists()
        assert (inbox / ".processed").exists()

    def test_watch_once_ingests_files(self, db, tmp_path):
        inbox = tmp_path / "inbox"
        setup_inbox(inbox)
        (inbox / "note.md").write_text("Hello from inbox")

        with patch.dict("os.environ", {}, clear=True):
            count = watch_once(db, inbox)

        assert count == 1
        assert not (inbox / "note.md").exists()  # moved to .processed
        assert (inbox / ".processed" / "note.md").exists()

    def test_watch_once_skips_hidden_files(self, db, tmp_path):
        inbox = tmp_path / "inbox"
        setup_inbox(inbox)
        (inbox / ".hidden").write_text("secret")

        count = watch_once(db, inbox)
        assert count == 0

    def test_watch_once_empty_inbox(self, db, tmp_path):
        inbox = tmp_path / "inbox"
        setup_inbox(inbox)
        count = watch_once(db, inbox)
        assert count == 0

    def test_watch_once_missing_inbox(self, db, tmp_path):
        count = watch_once(db, tmp_path / "nope")
        assert count == 0
