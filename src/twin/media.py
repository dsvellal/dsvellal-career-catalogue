"""Media storage: copy source files to data/media/<hash>.<ext> for recall."""

import mimetypes
import shutil
from pathlib import Path

DEFAULT_MEDIA_DIR = Path("./data/media")


def store_media(source_path: Path, content_hash: str, media_dir: Path = DEFAULT_MEDIA_DIR) -> str:
    """Copy a source file into managed media storage. Returns the relative path."""
    media_dir.mkdir(parents=True, exist_ok=True)
    ext = source_path.suffix.lower() or ".bin"
    dest_name = f"{content_hash}{ext}"
    dest_path = media_dir / dest_name
    if not dest_path.exists():
        shutil.copy2(source_path, dest_path)
    return dest_name


def get_media_path(content_hash: str, media_dir: Path = DEFAULT_MEDIA_DIR) -> Path | None:
    """Look up a stored media file by content hash prefix. Returns None if not found."""
    if not media_dir.exists():
        return None
    matches = list(media_dir.glob(f"{content_hash}.*"))
    return matches[0] if matches else None


def get_content_type(file_path: Path) -> str:
    """Detect MIME type from file extension."""
    mime, _ = mimetypes.guess_type(str(file_path))
    return mime or "application/octet-stream"
