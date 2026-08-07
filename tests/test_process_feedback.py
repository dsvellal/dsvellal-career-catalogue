"""Regression tests for professional-session feedback aggregation."""

from __future__ import annotations

import json
from pathlib import Path

from data.evidence.sessions.process_feedback import (
    compute_summary,
    regenerate_summary_from_json,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
SESSIONS_DIR = REPO_ROOT / "data" / "evidence" / "sessions"
GROW_PRE_SURVEY = (
    "28th Aug 2025 - GROW 3.0 - Unlocking the future with AI - "
    "Understanding our audience.(1-132).xlsx"
)


def _session(
    filename: str,
    *,
    responses: int,
    text_entries: int,
    ratings: list[tuple[int, int]],
    category: str = "dora",
    date: str = "2025-01-01",
    duplicate: bool = False,
    pre_survey: bool = False,
) -> dict:
    return {
        "filename": filename,
        "session_name": filename.removesuffix(".xlsx"),
        "date": date,
        "response_count": responses,
        "questions": [],
        "ratings": {
            f"rating-{index}": {
                "avg": float(scale - 1),
                "min": 1.0,
                "max": float(scale),
                "count": count,
                "scale": scale,
            }
            for index, (scale, count) in enumerate(ratings)
        },
        "text_feedback": [
            {
                "question": "What was valuable?",
                "response": f"Substantive feedback entry number {index} from {filename}",
            }
            for index in range(text_entries)
        ],
        "category": category,
        "is_pre_session_survey": pre_survey,
        "is_duplicate": duplicate,
        "raw_data_sample": [],
    }


def test_summary_partitions_duplicates_surveys_and_post_event_feedback():
    sessions = [
        _session(
            "post-event.xlsx",
            responses=3,
            text_entries=2,
            ratings=[(5, 3), (10, 2)],
        ),
        _session(
            "pre-survey.xlsx",
            responses=4,
            text_entries=1,
            ratings=[(10, 4)],
            category="ai-genai",
            pre_survey=True,
        ),
        _session(
            "duplicate.xlsx",
            responses=3,
            text_entries=1,
            ratings=[(5, 3)],
            duplicate=True,
        ),
    ]

    summary = compute_summary(sessions)

    assert summary["source_inventory"]["source_files"] == {
        "file_count": 3,
        "response_rows": 10,
        "qualitative_entries": 4,
        "rating_question_aggregates": 4,
        "rating_observations": 12,
    }
    assert summary["source_inventory"]["duplicates_excluded"]["file_count"] == 1
    assert summary["source_inventory"]["unique_files"]["response_rows"] == 7

    post_event = summary["analysis_populations"]["post_event_feedback"]
    assert post_event == {
        "file_count": 1,
        "response_rows": 3,
        "qualitative_entries": 2,
        "rating_question_aggregates": 2,
        "rating_observations": 5,
    }
    pre_surveys = summary["analysis_populations"]["pre_session_surveys"]
    assert pre_surveys["file_count"] == 1
    assert pre_surveys["response_rows"] == 4
    assert pre_surveys["filenames"] == ["pre-survey.xlsx"]

    assert summary["post_event_by_year"] == {
        "2025": {
            "file_count": 1,
            "response_rows": 3,
            "qualitative_entries": 2,
            "rating_question_aggregates": 2,
            "rating_observations": 5,
        }
    }
    assert set(summary["post_event_by_category"]) == {"dora"}
    assert summary["rating_inventory"]["question_level_aggregates"] == 2
    assert summary["rating_inventory"]["rating_observations"] == 5
    assert summary["rating_inventory"]["by_scale"] == {
        "5": {"question_level_aggregates": 1, "rating_observations": 3},
        "10": {"question_level_aggregates": 1, "rating_observations": 2},
    }

    serialized = json.dumps(summary).lower()
    assert "grand_average" not in serialized
    assert "satisfaction score" not in serialized
    assert all(quote["session"] == "post-event" for quote in summary["top_quotes"])


def test_committed_session_data_has_expected_population_counts():
    sessions = json.loads((SESSIONS_DIR / "all_sessions_data.json").read_text(encoding="utf-8"))

    summary = compute_summary(sessions)

    assert summary["source_inventory"] == {
        "source_files": {
            "file_count": 92,
            "response_rows": 1193,
            "qualitative_entries": 2023,
            "rating_question_aggregates": 228,
            "rating_observations": 2296,
        },
        "duplicates_excluded": {
            "file_count": 2,
            "response_rows": 10,
            "qualitative_entries": 20,
            "rating_question_aggregates": 5,
            "rating_observations": 16,
            "filenames": [
                "13th Sept 2019 - Code dojo session with Simao(1-2) (1).xlsx",
                "20190415 - Conducting interviews - knowledge sharing session(1-8) (1).xlsx",
            ],
        },
        "unique_files": {
            "file_count": 90,
            "response_rows": 1183,
            "qualitative_entries": 2003,
            "rating_question_aggregates": 223,
            "rating_observations": 2280,
        },
    }
    assert summary["analysis_populations"]["pre_session_surveys"] == {
        "file_count": 2,
        "response_rows": 133,
        "qualitative_entries": 192,
        "rating_question_aggregates": 2,
        "rating_observations": 131,
        "filenames": [
            "21st August 2025 - DORA for Software Leaders - Understanding the audience(1-1).xlsx",
            GROW_PRE_SURVEY,
        ],
    }
    assert summary["analysis_populations"]["post_event_feedback"] == {
        "file_count": 88,
        "response_rows": 1050,
        "qualitative_entries": 1811,
        "rating_question_aggregates": 221,
        "rating_observations": 2149,
    }
    assert {
        category: values["file_count"]
        for category, values in summary["post_event_by_category"].items()
    } == {
        "ai-genai": 23,
        "before-after": 2,
        "code-quality": 18,
        "connects": 2,
        "dora": 11,
        "feedback-about-datta": 9,
        "interview": 9,
        "other": 9,
        "tech-debt": 5,
    }


def test_committed_summary_matches_deterministic_json_regeneration(tmp_path: Path):
    input_path = SESSIONS_DIR / "all_sessions_data.json"
    output_path = tmp_path / "summary_stats.json"

    generated = regenerate_summary_from_json(input_path, output_path)
    first_bytes = output_path.read_bytes()
    regenerate_summary_from_json(input_path, output_path)

    assert output_path.read_bytes() == first_bytes
    assert json.loads(first_bytes) == generated
    assert generated == json.loads(
        (SESSIONS_DIR / "summary_stats.json").read_text(encoding="utf-8")
    )
