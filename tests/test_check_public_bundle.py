"""Tests for the post-build public-bundle publication boundary."""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts.check_public_bundle import REVIEWED_IMAGE_PREFIXES, check_public_bundle


def _valid_bundle(tmp_path: Path) -> Path:
    dist = tmp_path / "dist"
    assets = dist / "assets"
    assets.mkdir(parents=True)
    (dist / "index.html").write_text("<main>Public portfolio</main>", encoding="utf-8")
    (assets / "index-safe.js").write_text("const publicData = true;", encoding="utf-8")
    (assets / "index-safe.css").write_text("main { display: block; }", encoding="utf-8")
    extensions = {
        "photo-": ".jpg",
        "ibm-first-patent-invention-achievement-2010-": ".png",
        "ibm-rtle-2010-most-influential-tec-india-": ".png",
        "slide-27-": ".jpg",
    }
    assert set(extensions) == REVIEWED_IMAGE_PREFIXES
    for prefix, extension in extensions.items():
        (assets / f"{prefix}reviewed{extension}").write_bytes(b"reviewed-image")
    return dist


def test_accepts_only_the_reviewed_bundle_shape(tmp_path: Path):
    assert check_public_bundle(_valid_bundle(tmp_path)) == []


@pytest.mark.parametrize(
    ("payload", "expected"),
    [
        ("reviewer@example.org", "email address"),
        ("Call +1-248-555-0199", "phone number"),
        ("PAN ABCDE1234F", "PAN identifier"),
        ("Account number: 1234567890", "account value"),
        ("https://tenant.sharepoint.com/private", "SharePoint domain"),
        ("data/evidence/private-source.md", "raw evidence path"),
    ],
)
def test_rejects_private_text_in_any_emitted_text_asset(
    tmp_path: Path,
    payload: str,
    expected: str,
):
    dist = _valid_bundle(tmp_path)
    (dist / "assets" / "index-safe.js").write_text(payload, encoding="utf-8")

    assert any(expected in error for error in check_public_bundle(dist))


def test_rejects_unreviewed_files_directories_and_symlinks(tmp_path: Path):
    dist = _valid_bundle(tmp_path)
    (dist / "assets" / "unreviewed.png").write_bytes(b"private")
    (dist / "evidence").mkdir()
    (dist / "linked-private").symlink_to(dist / "evidence", target_is_directory=True)

    errors = check_public_bundle(dist)

    assert any("not an allowlisted public asset" in error for error in errors)
    assert any("unexpected directory" in error for error in errors)
    assert any("symlinks are forbidden" in error for error in errors)
