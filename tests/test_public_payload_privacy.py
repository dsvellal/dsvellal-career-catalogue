"""Defense-in-depth privacy checks for the emitted browser payload.

The portfolio compiler has its own allowlist and denylist.  This test deliberately
uses independent, payload-wide patterns so a private value cannot bypass those
checks by appearing in a title, excerpt, caveat, method, or other free-text field.
"""

from __future__ import annotations

import re
from collections.abc import Iterator
from typing import Any
from urllib.parse import urlparse

from scripts.build_portfolio_data import ALLOWED_EXTERNAL_HOSTS, build_portfolio_data

EMAIL_PATTERN = re.compile(r"(?i)(?<![\w.+-])[\w.+-]+@[a-z0-9.-]+\.[a-z]{2,}(?![\w.-])")
PHONE_PATTERN = re.compile(
    r"(?<!\w)(?:\+\d{1,3}[ .-])?(?:\(\d{2,4}\)|\d{2,4})"
    r"[ .-]\d{3,4}[ .-]\d{4}(?!\w)"
)
PAN_PATTERN = re.compile(r"(?<![A-Z0-9])[A-Z]{5}\d{4}[A-Z](?![A-Z0-9])")
ACCOUNT_VALUE_PATTERN = re.compile(
    r"(?i)\b(?:account|a/c|ac)\s*(?:no\.?|number|#)?\s*[:=-]\s*\d{6,}"
)
URL_PATTERN = re.compile(r"(?i)\b(?:https?://|mailto:)[^\s<>\"]+")
SECRET_VALUE_PATTERN = re.compile(
    r"(?i)\b(?:api[ _-]?key|access[ _-]?token|client[ _-]?secret|password)"
    r"\s*[:=]\s*\S+"
)

PRIVATE_SUBSTRINGS = (
    "/users/",
    "\\users\\",
    "file://",
    "data/evidence/",
    "data/exports/",
    "evidence_file",
    "teams.microsoft.com",
    "engage.cloud.microsoft",
    "safelinks.protection.outlook.com",
    "sharepoint.com",
    "docs.philips.com",
    "philips-internal",
    "service-now",
)


def _strings(value: Any, path: tuple[str, ...] = ()) -> Iterator[tuple[tuple[str, ...], str]]:
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for key, child in value.items():
            yield from _strings(child, (*path, str(key)))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _strings(child, (*path, str(index)))


def _privacy_violations(payload: Any) -> list[str]:
    violations: list[str] = []
    for path, value in _strings(payload):
        location = ".".join(path) or "$"
        lowered = value.lower()

        for label, pattern in (
            ("email address", EMAIL_PATTERN),
            ("phone number", PHONE_PATTERN),
            ("PAN identifier", PAN_PATTERN),
            ("account value", ACCOUNT_VALUE_PATTERN),
            ("secret value", SECRET_VALUE_PATTERN),
        ):
            if pattern.search(value):
                violations.append(f"{location}: contains {label}")

        for token in PRIVATE_SUBSTRINGS:
            if token in lowered:
                violations.append(f"{location}: contains private token {token!r}")

        urls = URL_PATTERN.findall(value)
        if not urls:
            continue
        if not path or path[-1] != "external_url" or len(urls) != 1 or urls[0] != value:
            violations.append(f"{location}: URL is outside the external_url field")
            continue
        parsed = urlparse(value)
        if (
            parsed.scheme != "https"
            or parsed.hostname not in ALLOWED_EXTERNAL_HOSTS
            or parsed.username
            or parsed.password
        ):
            violations.append(f"{location}: external URL is not allowlisted")

    return violations


def test_public_payload_has_no_unreviewed_identifiers_paths_or_links():
    assert _privacy_violations(build_portfolio_data()) == []


def test_privacy_scan_catches_values_outside_known_literal_denylist():
    unsafe = {
        "excerpt": "Contact reviewer@example.org or +1-248-555-0199.",
        "note": "Internal: https://tenant.sharepoint.com/private",
        "identity": "PAN ABCDE1234F",
        "credential": "access_token=not-a-real-token",
        "account": "Account number: 1234567890",
        "path": r"C:\Users\person\private.txt",
    }

    violations = _privacy_violations(unsafe)

    assert any("email address" in item for item in violations)
    assert any("phone number" in item for item in violations)
    assert any("URL is outside" in item for item in violations)
    assert any("sharepoint.com" in item for item in violations)
    assert any("PAN identifier" in item for item in violations)
    assert any("secret value" in item for item in violations)
    assert any("account value" in item for item in violations)
    assert any("\\\\users\\\\" in item for item in violations)
