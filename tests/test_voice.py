"""Tests for voice profile management."""

from pathlib import Path

import pytest

from twin.db import get_connection, init_schema
from twin.synthesis.voice import (
    build_system_prompt,
    create_profile,
    get_active_profile,
)


@pytest.fixture
def db(tmp_path: Path):
    db_path = tmp_path / "test.duckdb"
    init_schema(db_path)
    conn = get_connection(db_path)
    yield conn
    conn.close()


class TestCreateProfile:
    def test_creates_first_profile(self, db):
        profile = create_profile(db, profile_text="I am a builder.")
        assert profile.version == 1
        assert profile.active is True
        assert profile.profile_text == "I am a builder."

    def test_increments_version(self, db):
        create_profile(db, profile_text="V1")
        p2 = create_profile(db, profile_text="V2")
        assert p2.version == 2

    def test_deactivates_previous(self, db):
        create_profile(db, profile_text="V1")
        create_profile(db, profile_text="V2")
        active = db.execute("SELECT COUNT(*) FROM voice_profile WHERE active = TRUE").fetchone()
        assert active[0] == 1

    def test_default_profile_text(self, db):
        profile = create_profile(db)
        assert "software engineer" in profile.profile_text.lower()

    def test_stores_writing_samples(self, db):
        samples = ["I built systems that scale.", "My approach is evidence-driven."]
        profile = create_profile(db, writing_samples=samples)
        assert profile.writing_samples == samples

    def test_stores_tone_parameters(self, db):
        tone = {"style": "direct"}
        profile = create_profile(db, tone_parameters=tone)
        assert profile.tone_parameters == tone


class TestGetActiveProfile:
    def test_returns_none_when_no_profile(self, db):
        assert get_active_profile(db) is None

    def test_returns_active_profile(self, db):
        create_profile(db, profile_text="Active one")
        profile = get_active_profile(db)
        assert profile is not None
        assert profile.profile_text == "Active one"

    def test_returns_latest_active(self, db):
        create_profile(db, profile_text="First")
        create_profile(db, profile_text="Second")
        profile = get_active_profile(db)
        assert profile.profile_text == "Second"


class TestBuildSystemPrompt:
    def test_with_profile(self, db):
        profile = create_profile(db, profile_text="I focus on ML systems.")
        prompt = build_system_prompt(profile, audience="hiring_manager")
        assert "first person" in prompt.lower()
        assert "Datta Vellal" in prompt
        assert "I focus on ML systems." in prompt
        assert "hiring_manager" in prompt

    def test_without_profile(self):
        prompt = build_system_prompt(None, audience="peer_engineer")
        assert "first person" in prompt.lower()
        assert "Datta Vellal" in prompt
        assert "peer_engineer" in prompt

    def test_audience_adaptation(self, db):
        profile = create_profile(db)
        prompt = build_system_prompt(profile, audience="non_technical")
        assert "avoid" in prompt.lower()
