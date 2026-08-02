"""Tests for media storage and retrieval."""

from pathlib import Path

import pytest

from twin.media import get_content_type, get_media_path, store_media


@pytest.fixture
def media_dir(tmp_path: Path) -> Path:
    return tmp_path / "media"


@pytest.fixture
def sample_image(tmp_path: Path) -> Path:
    img = tmp_path / "cert.jpg"
    img.write_bytes(b"\xff\xd8\xff\xe0" + b"\x00" * 100)
    return img


class TestStoreMedia:
    def test_copies_file_to_media_dir(self, sample_image, media_dir):
        result = store_media(sample_image, "abc123hash", media_dir)
        assert result == "abc123hash.jpg"
        stored = media_dir / "abc123hash.jpg"
        assert stored.exists()
        assert stored.read_bytes() == sample_image.read_bytes()

    def test_preserves_extension(self, tmp_path, media_dir):
        pdf = tmp_path / "doc.pdf"
        pdf.write_bytes(b"%PDF-1.4" + b"\x00" * 50)
        result = store_media(pdf, "hashvalue", media_dir)
        assert result == "hashvalue.pdf"

    def test_uses_bin_for_no_extension(self, tmp_path, media_dir):
        no_ext = tmp_path / "mystery"
        no_ext.write_bytes(b"\x00" * 50)
        result = store_media(no_ext, "hashval", media_dir)
        assert result == "hashval.bin"

    def test_idempotent_no_overwrite(self, sample_image, media_dir):
        store_media(sample_image, "hash1", media_dir)
        stored = media_dir / "hash1.jpg"
        mtime_first = stored.stat().st_mtime

        store_media(sample_image, "hash1", media_dir)
        mtime_second = stored.stat().st_mtime
        assert mtime_first == mtime_second

    def test_creates_media_dir_if_missing(self, sample_image, tmp_path):
        nested_dir = tmp_path / "deep" / "nested" / "media"
        store_media(sample_image, "hash2", nested_dir)
        assert (nested_dir / "hash2.jpg").exists()


class TestGetMediaPath:
    def test_finds_stored_file(self, sample_image, media_dir):
        store_media(sample_image, "findhash", media_dir)
        result = get_media_path("findhash", media_dir)
        assert result is not None
        assert result.name == "findhash.jpg"

    def test_returns_none_for_missing(self, media_dir):
        media_dir.mkdir(parents=True, exist_ok=True)
        result = get_media_path("nonexistent", media_dir)
        assert result is None

    def test_returns_none_if_dir_missing(self, tmp_path):
        result = get_media_path("anything", tmp_path / "nope")
        assert result is None


class TestGetContentType:
    def test_jpg(self, tmp_path):
        assert get_content_type(tmp_path / "photo.jpg") == "image/jpeg"

    def test_pdf(self, tmp_path):
        assert get_content_type(tmp_path / "doc.pdf") == "application/pdf"

    def test_png(self, tmp_path):
        assert get_content_type(tmp_path / "img.png") == "image/png"

    def test_unknown(self, tmp_path):
        assert get_content_type(tmp_path / "blob.qzx7") == "application/octet-stream"
