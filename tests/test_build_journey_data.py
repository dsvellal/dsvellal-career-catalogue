"""Tests for the curated, public-safe Journey Atlas dataset."""

from __future__ import annotations

import json
import re
from pathlib import Path

from scripts.build_journey_data import (
    REPO_ROOT,
    build_journey_data,
    validate_journey_data,
    write_outputs,
)


def _walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk(child)


def test_committed_journey_data_is_deterministic_and_valid():
    generated = build_journey_data()
    committed_path = REPO_ROOT / "viz" / "src" / "data" / "journey.json"
    committed = json.loads(committed_path.read_text(encoding="utf-8"))

    assert committed == generated
    validate_journey_data(committed, REPO_ROOT)


def test_journey_has_exactly_eight_evidence_bound_views():
    data = build_journey_data()
    views = data["meta"]["views"]

    assert [view["id"] for view in views] == [
        "portrait",
        "journey",
        "capabilities",
        "outcomes",
        "respect",
        "influence",
        "service",
        "momentum",
    ]
    assert all(view["data_keys"] for view in views)
    assert all(key in data for view in views for key in view["data_keys"])


def test_public_dataset_preserves_provenance_without_private_payloads():
    data = build_journey_data()
    serialized = json.dumps(data, ensure_ascii=False).lower()

    assert "@philips.com" not in serialized
    assert "http://" not in serialized
    assert "https://" not in serialized
    assert "pan card" not in serialized
    assert "account number" not in serialized
    assert data["respect"]["recommendation_count"] == 20
    assert len(data["respect"]["recommendation_manifest"]) == 20

    assert "data/evidence/" not in serialized
    assert "evidence_file" not in serialized

    references = [item for item in _walk(data) if "source_id" in item]
    assert references
    assert {item["tier"] for item in references} >= {
        "corroborated",
        "documented",
        "self-reported",
        "derived",
    }
    assert all(re.fullmatch(r"src_[0-9a-f]{12}", item["source_id"]) for item in references)
    assert all(item["supports"] for item in references)


def test_claim_boundaries_and_chronology_are_explicit():
    data = build_journey_data()

    assert [(era["organization"], era["start"], era["end"]) for era in data["eras"]] == [
        ("IBM", 2007, 2013),
        ("Exeter Group", 2013, 2015),
        ("Amazon", 2016, 2018),
        ("Philips India", 2018, 2021),
        ("Philips North America", 2021, 2026),
    ]
    assert "team_attribution" in data["caveats"]
    assert "self_reported" in data["caveats"]
    assert "cooccurrence_not_influence" in data["caveats"]
    assert "future_direction" in data["caveats"]

    metrics = [item for item in _walk(data) if {"label", "display", "value"} <= set(item)]
    assert metrics
    assert all(item["evidence"] for item in metrics)

    impact_scopes = [item["scope"] for item in data["impact_ledger"]]
    assert impact_scopes.count("individual") == 1
    assert impact_scopes.count("team") == 1
    assert impact_scopes.count("organization") == 2
    assert impact_scopes.count("ecosystem") + impact_scopes.count("community") == 4


def test_writer_emits_json_and_analysis(tmp_path: Path):
    output = tmp_path / "journey.json"
    report = tmp_path / "journey-analysis.md"

    write_outputs(build_journey_data(), output, report)

    assert json.loads(output.read_text(encoding="utf-8"))["meta"]["schema_version"] == 1
    report_text = report.read_text(encoding="utf-8")
    assert "Why these eight views are the strongest projection" in report_text
    assert "builder" in report_text
    assert "organizational multiplier" in report_text
