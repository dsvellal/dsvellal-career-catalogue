"""Contract tests for the public, auditable executive-portfolio dataset."""

from __future__ import annotations

import copy
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

import pytest

import scripts.build_portfolio_data as portfolio_builder
from scripts.build_portfolio_data import (
    ALLOWED_EXTERNAL_HOSTS,
    FORBIDDEN_PUBLIC_TOKENS,
    REPO_ROOT,
    SOURCE_SPECS,
    build_portfolio_data,
    validate_portfolio_data,
    write_portfolio_data,
)


def _by_id(records):
    return {record["id"]: record for record in records}


def _strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from _strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from _strings(child)


def test_committed_portfolio_is_deterministic_and_valid():
    generated = build_portfolio_data()
    committed_path = REPO_ROOT / "viz" / "src" / "data" / "portfolio.json"
    committed = json.loads(committed_path.read_text(encoding="utf-8"))

    assert committed == generated
    validate_portfolio_data(committed)


def test_portfolio_uses_the_eight_route_executive_information_architecture():
    data = build_portfolio_data()

    assert [(page["id"], page["route"]) for page in data["pages"]] == [
        ("brief", "brief"),
        ("leadership", "leadership"),
        ("journey", "journey"),
        ("trust", "trust"),
        ("innovation", "innovation"),
        ("learning", "learning"),
        ("community", "community"),
        ("data-room", "data-room"),
    ]
    assert _by_id(data["pages"])["innovation"]["label"] == "Innovation & value"
    data_room = _by_id(data["pages"])["data-room"]
    assert data_room["claim_ids"] == data["audit_only_claim_ids"]
    assert data["audit_only_claim_ids"] == [
        "claim-evidence-corpus-coverage",
        "claim-export-embedding-gap",
        "claim-export-provenance-gap",
        "claim-professional-community-trust-bridge",
    ]
    assert data["executive_semantics"]["page_copy"]["innovation"] == {
        "question": "How does Datta turn emerging technology into governed execution?",
        "summary": (
            "A record of carrying ideas from invention through engineered delivery "
            "while framing opportunity at portfolio scale."
        ),
    }


def test_story_blocks_are_the_exact_single_owner_55_claim_hierarchy():
    data = build_portfolio_data()
    expected = [
        (
            "brief-influence-beyond-hierarchy",
            "brief",
            "claim-title-independent-leadership-continuity",
            [],
        ),
        ("brief-speed-built-on-discipline", "brief", "claim-quality-before-ai-lineage", []),
        (
            "brief-capability-that-multiplies",
            "brief",
            "claim-learn-build-teach-systemize-pattern",
            [],
        ),
        ("brief-service-that-compounds", "brief", "claim-service-continuity-and-growth", []),
        (
            "leadership-boundaries",
            "leadership",
            "claim-2025-cross-boundary-leadership",
            ["claim-2015-cross-team-leadership"],
        ),
        (
            "leadership-benchmark",
            "leadership",
            "claim-2020-360-company-deltas",
            ["claim-2020-strengths-profile", "claim-strengths-later-observation-concordance"],
        ),
        (
            "leadership-growth",
            "leadership",
            "claim-feedback-to-executive-observation",
            [
                "claim-2020-executive-influence-development-signal",
                "claim-2025-executive-influence-observation",
            ],
        ),
        ("journey-span", "journey", "claim-career-calendar-span", ["claim-2008-early-leadership"]),
        ("journey-community", "journey", "claim-2010-technical-community-recognition", []),
        ("journey-delivery", "journey", "claim-2017-process-delivery-recognition", []),
        ("journey-enterprise", "journey", "claim-2021-cto-recognition", []),
        ("trust-sought-out", "trust", "claim-connect-demand-share", ["claim-connect-volume-2021"]),
        ("trust-independent-thinkers", "trust", "claim-2020-mentoring-method", []),
        ("trust-purpose", "trust", "claim-2023-purpose-first-mentoring", []),
        (
            "innovation-patent",
            "innovation",
            "claim-public-patent-record",
            ["claim-2010-first-patent-achievement"],
        ),
        (
            "innovation-controlled-ai",
            "innovation",
            "claim-sutra-ai-delivery",
            [
                "claim-sutra-traceability",
                "claim-sutra-delivery-recognition",
                "claim-2015-quality-discipline",
                "claim-2020-quality-speed-framing",
            ],
        ),
        (
            "innovation-portfolio-value",
            "innovation",
            "claim-xite-potential-efficiency",
            ["claim-xite-potential-hours"],
        ),
        (
            "learning-listening-system",
            "learning",
            "claim-session-post-responses",
            [
                "claim-session-post-datasets",
                "claim-session-rating-observations",
                "claim-session-qualitative-entries",
                "claim-session-audience-surveys",
            ],
        ),
        ("learning-reach", "learning", "claim-community-talks-reach", []),
        (
            "learning-valued",
            "learning",
            "claim-student-presenter-ratings",
            [
                "claim-student-feedback-coverage",
                "claim-student-recommendation-likelihood",
                "claim-student-takeaway-interview-resilience-2017",
                "claim-student-takeaway-uncertainty-2020",
            ],
        ),
        (
            "learning-frontier",
            "learning",
            "claim-topic-frontier-teaching-continuity",
            [
                "claim-feedback-adaptation-tension",
                "claim-session-ai-feedback",
                "claim-session-dora-feedback",
                "claim-2019-practical-feedback-request",
                "claim-2024-practical-ai-takeaway",
                "claim-2026-hands-on-depth-request",
            ],
        ),
        ("community-presence", "community", "claim-community-service-photo-record", []),
        (
            "community-scaled-giving",
            "community",
            "claim-book-program-total",
            ["claim-book-program-growth"],
        ),
    ]
    actual = [
        (
            block["id"],
            block["page_id"],
            block["primary_claim_id"],
            block["folded_claim_ids"],
        )
        for block in data["story_blocks"]
    ]
    assert actual == expected

    story_claims = [
        claim_id
        for block in data["story_blocks"]
        for claim_id in [block["primary_claim_id"], *block["folded_claim_ids"]]
    ]
    assert len(story_claims) == len(set(story_claims)) == 51
    assert set(story_claims) | set(data["audit_only_claim_ids"]) == {
        claim["id"] for claim in data["claims"]
    }
    block_counts = Counter(block["page_id"] for block in data["story_blocks"])
    assert block_counts == {
        "brief": 4,
        "leadership": 3,
        "journey": 4,
        "trust": 3,
        "innovation": 3,
        "learning": 4,
        "community": 2,
    }
    assert "image_source_id" not in _by_id(data["story_blocks"])["innovation-patent"]
    assert _by_id(data["story_blocks"])["community-presence"]["image_source_id"] == (
        "source-community-service-photo-record-2007-2015"
    )
    assert all(
        not re.search(r"\b(?:not|gaps?|confidence|rows?|files?|ledger)\b", block["title"], re.I)
        for block in data["story_blocks"]
    )


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (
            lambda data: data["story_blocks"][0].update({"primary_claim_id": "claim-unknown"}),
            "unknown primary claim",
        ),
        (
            lambda data: data["story_blocks"][0].update({"title": "Confidence gap ledger"}),
            "banned language",
        ),
        (
            lambda data: data["story_blocks"][0]["folded_claim_ids"].append(
                data["story_blocks"][1]["primary_claim_id"]
            ),
            "multiple story blocks",
        ),
        (
            lambda data: data["story_blocks"].pop(),
            "two to four story blocks",
        ),
    ],
)
def test_validator_rejects_invalid_story_hierarchy(mutation, message):
    data = copy.deepcopy(build_portfolio_data())
    mutation(data)

    with pytest.raises(ValueError, match=message):
        validate_portfolio_data(data)


def test_corrected_feedback_populations_and_units_are_exact():
    data = build_portfolio_data()
    claims = _by_id(data["claims"])

    assert claims["claim-session-post-datasets"]["metric"] == {
        "value": 88,
        "display": "88 analysis files",
        "unit": "files",
    }
    assert claims["claim-session-post-responses"]["metric"]["value"] == 1050
    assert claims["claim-session-rating-observations"]["metric"]["value"] == 2149
    assert claims["claim-session-qualitative-entries"]["metric"]["value"] == 1811
    assert claims["claim-session-audience-surveys"]["metric"] == {
        "value": 133,
        "display": "2 surveys · 133 rows",
        "unit": "response rows",
    }
    assert claims["claim-session-ai-feedback"]["metric"] == {
        "value": 23,
        "display": "23 files · 288 rows",
        "unit": "files",
    }
    assert claims["claim-session-dora-feedback"]["metric"] == {
        "value": 11,
        "display": "11 files · 79 rows",
        "unit": "files",
    }
    assert "facilitated sessions" in claims["claim-session-post-datasets"]["statement"]


def test_required_calculations_publish_inputs_formula_and_limits():
    data = build_portfolio_data()
    claims = _by_id(data["claims"])
    methods = _by_id(data["methods"])

    assert claims["claim-career-calendar-span"]["metric"]["value"] == 20
    assert (
        "not tenure" in _by_id(data["caveats"])["caveat-calendar-span-not-tenure"]["label"].lower()
    )

    assert claims["claim-connect-demand-share"]["metric"]["value"] == 79
    connect_inputs = _by_id(methods["method-connect-demand-v1"]["inputs"])
    assert connect_inputs["input-connect-total"]["value"] == 575
    assert connect_inputs["input-connect-requested"]["value"] == 454
    assert "requested_by_others" in methods["method-connect-demand-v1"]["formula"]

    assert claims["claim-book-program-total"]["metric"]["value"] == 1_972_381
    assert claims["claim-book-program-growth"]["metric"]["value"] == 13.3
    service = claims["claim-service-continuity-and-growth"]
    assert "no program is recorded for 2020–2021" in service["statement"]
    assert "no reviewed 2024 program record is present" in service["statement"]
    assert "not uninterrupted activity" in service["statement"]
    book_inputs = _by_id(methods["method-book-totals-growth-v1"]["inputs"])
    assert book_inputs["input-book-unrecorded-years"]["value"] == "2020–2021 and 2024"
    assert any(
        "Do not imply uninterrupted activity after the 2022 resumption" in rule
        for rule in methods["method-book-totals-growth-v1"]["exclusion_rules"]
    )
    assert (
        "no reviewed 2024 program record"
        in methods["method-service-continuity-growth-v1"]["result"]
    )

    assert claims["claim-2020-360-company-deltas"]["metric"] == {
        "value": 0.31,
        "display": "+0.31 mean delta",
        "unit": "rating points vs company average",
    }
    assert "+0.24" in claims["claim-2020-360-company-deltas"]["statement"]
    assert "+0.39" in claims["claim-2020-360-company-deltas"]["statement"]


def test_every_claim_and_relationship_is_source_linked_and_method_bound():
    data = build_portfolio_data()
    claims = _by_id(data["claims"])
    supports = _by_id(data["supports"])
    methods = _by_id(data["methods"])

    for claim in data["claims"]:
        assert claim["support_ids"]
        assert all(supports[item]["claim_id"] == claim["id"] for item in claim["support_ids"])
        if claim["kind"] in {"calculated", "interpreted"}:
            assert claim["method_id"] in methods
            assert methods[claim["method_id"]]["inputs"]

    assert len(data["relationships"]) == 11
    for relationship in data["relationships"]:
        assert relationship["from_claim_id"] in claims
        assert relationship["to_claim_id"] in claims
        assert relationship["claim_id"] in claims
        assert relationship["method_id"] in methods
        assert relationship["support_ids"] == claims[relationship["claim_id"]]["support_ids"]
        assert relationship["limitation"]
        assert relationship["confidence"]["rationale"]

    assert {
        "relationship-patent-application-to-grant",
        "relationship-feedback-to-executive-observation",
        "relationship-strengths-to-observed-behavior",
        "relationship-quality-before-ai",
        "relationship-title-independent-leadership",
        "relationship-learn-build-teach-systemize",
        "relationship-topic-frontier-continuity",
        "relationship-connect-demand-composition",
        "relationship-service-continuity-growth",
        "relationship-professional-community-trust-bridge",
        "relationship-feedback-adaptation-tension",
    } == {relationship["id"] for relationship in data["relationships"]}


def test_participant_takeaways_and_requests_are_explicit_verbatim_sources():
    data = build_portfolio_data()
    claims = _by_id(data["claims"])
    supports = _by_id(data["supports"])
    sources = _by_id(data["sources"])

    expected_categories = {
        "claim-2019-practical-feedback-request": "requested_improvement",
        "claim-2024-practical-ai-takeaway": "participant_takeaway",
        "claim-2026-hands-on-depth-request": "requested_improvement",
        "claim-student-takeaway-interview-resilience-2017": "participant_takeaway",
        "claim-student-takeaway-uncertainty-2020": "participant_takeaway",
    }
    for claim_id, category in expected_categories.items():
        claim = claims[claim_id]
        assert claim["category"] == category
        assert claim["status"] == "published"
        claim_sources = {
            sources[supports[support_id]["source_id"]]["id"] for support_id in claim["support_ids"]
        }
        assert len(claim_sources) == 1
        selected = sources[claim_sources.pop()]
        assert selected["source_type"] == "selected_anonymous_feedback"
        assert selected["excerpt_kind"] == "verbatim"

    for spec in SOURCE_SPECS:
        if spec.get("excerpt_kind") != "verbatim":
            continue
        held_data = json.loads((REPO_ROOT / spec["path"]).read_text(encoding="utf-8"))
        assert any(spec["approved_excerpt"] in value for value in _strings(held_data))


def test_builder_rejects_a_verbatim_excerpt_not_in_the_canonical_source(monkeypatch):
    altered_specs = []
    target_id = "source-student-takeaway-uncertainty-2020"
    for spec in SOURCE_SPECS:
        altered = dict(spec)
        if spec["id"] == target_id:
            altered["approved_excerpt"] += " text that is not in the source"
        altered_specs.append(altered)

    monkeypatch.setattr(portfolio_builder, "SOURCE_SPECS", tuple(altered_specs))

    with pytest.raises(ValueError, match=f"canonical source: {target_id}"):
        portfolio_builder.build_portfolio_data()


def test_student_feedback_is_separate_scale_safe_and_present_on_learning_pages():
    data = build_portfolio_data()
    claims = _by_id(data["claims"])
    methods = _by_id(data["methods"])
    pages = _by_id(data["pages"])
    method = methods["method-student-feedback-aggregate-v1"]
    inputs = _by_id(method["inputs"])

    assert claims["claim-student-feedback-coverage"]["metric"] == {
        "value": 494,
        "display": "13 forms · 494 response rows",
        "unit": "response rows",
    }
    assert inputs["input-student-institutions"]["value"] == 6
    assert inputs["input-student-corporate-context"]["value"] == 1
    assert inputs["input-student-presenter-5"] == {
        "id": "input-student-presenter-5",
        "label": "Presenter mean on 5-point forms",
        "source_id": "source-student-feedback-structured-corpus-2013-2020",
        "locator": "presenter aggregates with source scale /5",
        "value": 4.58,
        "unit": "/5, n=149",
    }
    assert inputs["input-student-presenter-10"]["value"] == 9.12
    assert inputs["input-student-presenter-10"]["unit"] == "/10, n=128"
    assert inputs["input-student-recommendation"]["value"] == 8.87
    assert inputs["input-student-recommendation"]["unit"] == "/10, n=98"
    assert claims["claim-student-recommendation-likelihood"]["title"] == (
        "Recommendation likelihood averaged 8.87/10"
    )
    assert "original source scale" in claims["claim-student-recommendation-likelihood"]["statement"]
    assert any("Do not publish raw rows" in rule for rule in method["exclusion_rules"])

    student_claim_ids = {
        "claim-student-feedback-coverage",
        "claim-student-presenter-ratings",
        "claim-student-recommendation-likelihood",
        "claim-student-takeaway-interview-resilience-2017",
        "claim-student-takeaway-uncertainty-2020",
    }
    assert student_claim_ids <= set(pages["learning"]["claim_ids"])
    assert student_claim_ids.isdisjoint(pages["community"]["claim_ids"])
    assert "1050" not in method["result"]
    assert "3,732" not in method["result"]

    supports = _by_id(data["supports"])
    nie_support = supports[
        claims["claim-student-takeaway-interview-resilience-2017"]["support_ids"][0]
    ]
    sit_support = supports[claims["claim-student-takeaway-uncertainty-2020"]["support_ids"][0]]
    assert nie_support["locator"].endswith("feedback.key_takeaways[0] (same text also at [1])")
    assert sit_support["locator"].endswith("feedback.key_takeaways[31]")


def test_xite_portfolio_and_sutra_initiative_scopes_never_blur():
    data = build_portfolio_data()
    claims = _by_id(data["claims"])
    conflicts = _by_id(data["conflicts"])

    xite_claims = [
        claims["claim-xite-potential-hours"],
        claims["claim-xite-potential-efficiency"],
    ]
    assert all(claim["scope"] == "portfolio" for claim in xite_claims)
    assert all("potential" in claim["statement"].lower() for claim in xite_claims)
    assert all("caveat-potential-not-realized" in claim["caveat_ids"] for claim in xite_claims)

    sutra = claims["claim-sutra-ai-delivery"]
    assert sutra["scope"] == "team_initiative"
    assert "18,000" not in sutra["statement"]
    assert "€3.5" not in sutra["statement"]
    assert "zero compromise" not in sutra["statement"].lower()
    assert "commit" in sutra["statement"].lower()
    assert "conflict-sutra-onboarding-arithmetic" in sutra["conflict_ids"]
    assert "conflict-sutra-zero-quality-boundary" in sutra["conflict_ids"]
    assert conflicts["conflict-sutra-onboarding-arithmetic"]["status"] == "metric_withheld"
    assert (
        conflicts["conflict-sutra-zero-quality-boundary"]["status"]
        == "claim_bounded_to_observed_controls"
    )


def test_patent_award_to_public_grant_is_a_direct_observed_relationship():
    data = build_portfolio_data()
    claims = _by_id(data["claims"])
    supports = _by_id(data["supports"])
    methods = _by_id(data["methods"])
    relationships = _by_id(data["relationships"])
    pages = _by_id(data["pages"])

    achievement_id = "claim-2010-first-patent-achievement"
    public_patent_id = "claim-public-patent-record"
    relationship = relationships["relationship-patent-application-to-grant"]
    method = methods["method-patent-award-registry-match-v1"]
    inputs = _by_id(method["inputs"])

    assert claims[achievement_id]["kind"] == "observed"
    assert relationship["state"] == "observed"
    assert relationship["from_claim_id"] == achievement_id
    assert relationship["to_claim_id"] == public_patent_id
    assert all(
        supports[support_id]["directness"] == "direct" for support_id in relationship["support_ids"]
    )
    assert (
        inputs["input-patent-award-title"]["value"].casefold()
        == inputs["input-patent-registry-title"]["value"].casefold()
    )
    assert (
        inputs["input-patent-award-recipient"]["value"]
        == inputs["input-patent-registry-inventor"]["value"]
    )
    assert "one of three inventors" in method["result"]
    assert "sole inventorship" in relationship["limitation"]
    assert "commercialization" in relationship["limitation"]
    assert achievement_id not in pages["journey"]["claim_ids"]
    assert achievement_id in pages["innovation"]["claim_ids"]


def test_public_catalog_is_safe_stable_and_openable_where_external():
    data = build_portfolio_data()
    serialized = json.dumps(data, ensure_ascii=False).lower()

    for token in FORBIDDEN_PUBLIC_TOKENS:
        assert token not in serialized
    assert '"path"' not in serialized
    assert "evidence_file" not in serialized

    for source in data["sources"]:
        assert re.fullmatch(r"source-[a-z0-9-]+", source["id"])
        assert re.fullmatch(r"[0-9a-f]{64}", source["sha256"])
        assert source["excerpt_kind"] in {"verbatim", "editorial_summary"}
        assert source["approved_excerpt"]
        assert source["checksum_scope"] == "held_canonical_artifact"
        assert isinstance(source["checksum_note"], str) and source["checksum_note"]
        if url := source.get("external_url"):
            parsed = urlparse(url)
            assert parsed.scheme == "https"
            assert parsed.hostname in ALLOWED_EXTERNAL_HOSTS

    patent = _by_id(data["sources"])["source-us-patent-8560487"]
    assert patent["access_state"] == "public_external"
    assert patent["external_url"] == "https://patents.google.com/patent/US8560487B2/en"
    assert "not live external page content" in patent["checksum_note"]


def test_validator_rejects_an_ambiguous_external_source_checksum():
    data = copy.deepcopy(build_portfolio_data())
    patent = _by_id(data["sources"])["source-us-patent-8560487"]
    patent["checksum_scope"] = "live_external_page"
    patent["checksum_note"] = "SHA-256 of an unspecified object."

    with pytest.raises(ValueError, match="checksum scope"):
        validate_portfolio_data(data)


@pytest.mark.parametrize(
    "leak",
    [
        " owner@example.org",
        " +1 (555) 867-5309",
        " 9972312693",
        " https://private.example.org/source",
        " docs.philips.com/private-record",
    ],
)
def test_payload_wide_validator_rejects_contact_urls_and_internal_domains(leak):
    data = copy.deepcopy(build_portfolio_data())
    data["meta"]["subtitle"] += leak

    with pytest.raises(ValueError):
        validate_portfolio_data(data)


def test_data_quality_discloses_conflicts_and_export_gaps():
    data = build_portfolio_data()
    coverage = data["data_quality"]["coverage"]
    gaps = _by_id(data["data_quality"]["export_gaps"])

    assert coverage["evidence_markdown_files"] == 1086
    assert coverage["individual_evidence_records_excluding_indexes"] == 896
    assert coverage["informal_feedback_records_excluding_index"] == 137
    assert coverage["documentary_images"] == 377
    assert coverage["evidence_index_rows"] == 562
    assert gaps["gap-retrieval-index"]["count"] == 4411
    assert gaps["gap-edge-artifact-provenance"]["count"] == 13

    conflict_ids = {conflict["id"] for conflict in data["conflicts"]}
    assert {
        "conflict-session-population-accounting",
        "conflict-session-rating-units",
        "conflict-session-category-counts",
        "conflict-career-duration-labels",
        "conflict-jscpd-causality",
        "conflict-sutra-onboarding-arithmetic",
        "conflict-sutra-zero-quality-boundary",
    } <= conflict_ids


def test_writer_emits_valid_json(tmp_path: Path):
    output = tmp_path / "portfolio.json"
    data = build_portfolio_data()

    write_portfolio_data(data, output)

    written = json.loads(output.read_text(encoding="utf-8"))
    assert written == data
    assert written["meta"]["schema_version"] == 3
