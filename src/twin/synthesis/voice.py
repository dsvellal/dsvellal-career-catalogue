"""Voice profile management: create, store, and apply voice profiles."""

import json
import uuid
from dataclasses import dataclass, field

import duckdb

DEFAULT_VOICE_PROFILE = {
    "identity": {
        "perspective": "first_person",
        "tone": "professional_but_approachable",
        "technical_depth": "high",
        "self_presentation": "confident_not_boastful",
    },
    "boundaries": {
        "never_claim_without_evidence": True,
        "always_cite": True,
        "uncertainty_handling": "acknowledge gaps directly",
    },
    "audience_adaptations": {
        "technical_recruiter": {
            "emphasis": "skills, metrics, scale",
            "depth": "medium",
            "jargon": "use_freely",
        },
        "hiring_manager": {
            "emphasis": "impact, leadership, decision_making",
            "depth": "high",
            "jargon": "moderate",
        },
        "peer_engineer": {
            "emphasis": "technical_choices, tradeoffs, learnings",
            "depth": "deep",
            "jargon": "full",
        },
        "non_technical": {
            "emphasis": "outcomes, analogies, impact",
            "depth": "low",
            "jargon": "avoid",
        },
    },
}


@dataclass
class VoiceProfile:
    id: str
    version: int
    profile_text: str
    tone_parameters: dict = field(default_factory=dict)
    writing_samples: list[str] = field(default_factory=list)
    active: bool = True


def create_profile(
    conn: duckdb.DuckDBPyConnection,
    profile_text: str = "",
    writing_samples: list[str] | None = None,
    tone_parameters: dict | None = None,
) -> VoiceProfile:
    """Create a new voice profile version. Deactivates previous versions."""
    conn.execute("UPDATE voice_profile SET active = FALSE WHERE active = TRUE")

    current_max = conn.execute("SELECT MAX(version) FROM voice_profile").fetchone()
    version = (current_max[0] or 0) + 1 if current_max else 1

    profile_id = f"voice_{uuid.uuid4().hex[:8]}"
    samples = writing_samples or []
    tone = tone_parameters or DEFAULT_VOICE_PROFILE

    if not profile_text:
        profile_text = _generate_default_profile_text()

    conn.execute(
        "INSERT INTO voice_profile (id, version, profile_text, writing_samples, "
        "tone_parameters, active) VALUES (?, ?, ?, ?, ?, TRUE)",
        [profile_id, version, profile_text, json.dumps(samples), json.dumps(tone)],
    )

    return VoiceProfile(
        id=profile_id,
        version=version,
        profile_text=profile_text,
        tone_parameters=tone,
        writing_samples=samples,
    )


def get_active_profile(conn: duckdb.DuckDBPyConnection) -> VoiceProfile | None:
    """Get the currently active voice profile."""
    row = conn.execute(
        "SELECT id, version, profile_text, writing_samples, tone_parameters "
        "FROM voice_profile WHERE active = TRUE"
    ).fetchone()

    if not row:
        return None

    return VoiceProfile(
        id=row[0],
        version=row[1],
        profile_text=row[2],
        writing_samples=json.loads(row[3]) if row[3] else [],
        tone_parameters=json.loads(row[4]) if row[4] else {},
    )


def build_system_prompt(
    profile: VoiceProfile | None,
    audience: str = "peer_engineer",
) -> str:
    """Build a system prompt from the voice profile for LLM synthesis."""
    if not profile:
        return _default_system_prompt(audience)

    tone: dict = profile.tone_parameters or DEFAULT_VOICE_PROFILE  # type: ignore[assignment]
    adaptations: dict = tone.get("audience_adaptations", {})
    audience_config: dict = adaptations.get(audience, adaptations.get("peer_engineer", {}))

    return (
        "You are answering as Datta Vellal, speaking in first person.\n\n"
        f"Voice profile:\n{profile.profile_text}\n\n"
        f"Audience: {audience}\n"
        f"Emphasis: {audience_config.get('emphasis', 'balanced')}\n"
        f"Depth: {audience_config.get('depth', 'medium')}\n"
        f"Jargon level: {audience_config.get('jargon', 'moderate')}\n\n"
        "Rules:\n"
        "- Always speak in first person\n"
        "- Only claim things supported by provided evidence\n"
        "- Cite specific artifacts/projects when making claims\n"
        "- Acknowledge gaps directly rather than fabricating\n"
        "- Be confident but not boastful\n"
    )


def _default_system_prompt(audience: str) -> str:
    return (
        "You are answering as Datta Vellal, speaking in first person.\n\n"
        f"Audience: {audience}\n\n"
        "Rules:\n"
        "- Always speak in first person\n"
        "- Only claim things supported by provided evidence\n"
        "- Cite specific artifacts/projects when making claims\n"
        "- Acknowledge gaps directly rather than fabricating\n"
        "- Be confident but not boastful\n"
    )


def _generate_default_profile_text() -> str:
    return (
        "I am a software engineer with deep experience in knowledge systems, "
        "NLP, and ML engineering. I communicate clearly and technically, "
        "preferring concrete examples over abstractions. I focus on impact "
        "and measurable outcomes when describing my work."
    )
