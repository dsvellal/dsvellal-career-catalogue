#!/usr/bin/env python3
"""Reject private data and unreviewed files in the built public portfolio."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIST = REPO_ROOT / "viz" / "dist"

TEXT_SUFFIXES = {".html", ".js", ".css"}
REVIEWED_IMAGE_PREFIXES = {
    "photo-",
    "ibm-first-patent-invention-achievement-2010-",
    "ibm-rtle-2010-most-influential-tec-india-",
    "slide-27-",
}
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}

EMAIL_PATTERN = re.compile(r"(?i)(?<![\w.+-])[\w.+-]+@[a-z0-9.-]+\.[a-z]{2,}(?![\w.-])")
PHONE_PATTERN = re.compile(
    r"(?<!\w)(?:\+\d{1,3}[ .-])?(?:\(\d{2,4}\)|\d{2,4})"
    r"[ .-]\d{3,4}[ .-]\d{4}(?!\w)"
)
PAN_PATTERN = re.compile(r"(?<![A-Z0-9])[A-Z]{5}\d{4}[A-Z](?![A-Z0-9])")
ACCOUNT_VALUE_PATTERN = re.compile(
    r"(?i)\b(?:account|a/c|ac)\s*(?:no\.?|number|#)?\s*[:=-]\s*\d{6,}"
)
PRIVATE_TEXT_TOKENS = {
    "/users/": "local user path",
    "\\users\\": "local user path",
    "file://": "local file URL",
    "data/evidence/": "raw evidence path",
    "data/exports/": "raw export path",
    "evidence_file": "private evidence field",
    "mailto:": "email link",
    "teams.microsoft.com": "internal Teams domain",
    "engage.cloud.microsoft": "internal Engage domain",
    "safelinks.protection.outlook.com": "authentication-bearing Safe Links domain",
    "sharepoint.com": "SharePoint domain",
    "docs.philips.com": "internal document domain",
    "gitlab.ta.philips.com": "internal GitLab domain",
    "philips-internal": "internal Philips domain",
    "service-now": "internal service domain",
    "account number": "account-number language",
    "pan card": "PAN-card language",
}


def _scan_text(path: Path, relative: str) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lowered = text.lower()
    errors: list[str] = []

    for label, pattern in (
        ("email address", EMAIL_PATTERN),
        ("phone number", PHONE_PATTERN),
        ("PAN identifier", PAN_PATTERN),
        ("account value", ACCOUNT_VALUE_PATTERN),
    ):
        if pattern.search(text):
            errors.append(f"{relative}: contains {label}")

    for token, label in PRIVATE_TEXT_TOKENS.items():
        if token in lowered:
            errors.append(f"{relative}: contains {label} ({token!r})")

    return errors


def check_public_bundle(dist: Path) -> list[str]:
    """Return publication-boundary violations found below ``dist``."""
    errors: list[str] = []
    if dist.is_symlink():
        return [f"{dist}: bundle root must not be a symlink"]
    if not dist.is_dir():
        return [f"{dist}: bundle directory does not exist"]

    seen_images: dict[str, int] = {prefix: 0 for prefix in REVIEWED_IMAGE_PREFIXES}
    seen_html = False
    seen_js = False
    seen_css = False

    for path in sorted(dist.rglob("*")):
        relative = path.relative_to(dist).as_posix()
        if path.is_symlink():
            errors.append(f"{relative}: symlinks are forbidden in the public bundle")
            continue
        if path.is_dir():
            if relative != "assets":
                errors.append(f"{relative}: unexpected directory in the public bundle")
            continue
        if not path.is_file():
            errors.append(f"{relative}: unsupported filesystem entry")
            continue

        suffix = path.suffix.lower()
        if suffix in TEXT_SUFFIXES:
            if suffix == ".html":
                seen_html = True
                if relative != "index.html":
                    errors.append(f"{relative}: index.html is the only allowed HTML file")
            elif suffix == ".js":
                seen_js = True
            elif suffix == ".css":
                seen_css = True
            errors.extend(_scan_text(path, relative))
            continue

        matched_prefix = next(
            (prefix for prefix in REVIEWED_IMAGE_PREFIXES if path.name.startswith(prefix)),
            None,
        )
        if (
            suffix not in IMAGE_SUFFIXES
            or path.parent != dist / "assets"
            or matched_prefix is None
        ):
            errors.append(f"{relative}: file is not an allowlisted public asset")
            continue
        seen_images[matched_prefix] += 1

    for required, seen in (("index.html", seen_html), ("JavaScript", seen_js), ("CSS", seen_css)):
        if not seen:
            errors.append(f"bundle is missing required {required}")
    for prefix, count in sorted(seen_images.items()):
        if count != 1:
            errors.append(
                f"reviewed image prefix {prefix!r} must occur exactly once; found {count}"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dist", nargs="?", type=Path, default=DEFAULT_DIST)
    args = parser.parse_args()

    errors = check_public_bundle(args.dist)
    if errors:
        print("Public bundle rejected:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Public bundle accepted: {args.dist}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
