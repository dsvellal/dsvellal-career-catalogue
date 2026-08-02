"""AI-powered document classification via Gemini."""

import json
import os
from dataclasses import dataclass, field

from google import genai
from google.genai import types

CLASSIFICATION_PROMPT = (  # noqa: E501
    "You are classifying a document for a personal knowledge system.\n\n"
    "Given this extracted text from a {file_type} file:\n"
    "---\n{text_preview}\n---\n\n"
    "Classify this artifact:\n"
    "1. What type is this? (email_appreciation|certificate|project_doc|"
    "meeting_notes|code_readme|performance_review|recommendation|presentation|other)\n"
    "2. What time period does it reference? (extract dates as ISO 8601)\n"
    "3. What projects are mentioned or implied?\n"
    "4. What skills/technologies are demonstrated?\n"
    "5. What people are mentioned and in what capacity?\n"
    "6. What organizations are mentioned and in what role? "
    "(employer|issuer|client|partner|education)\n"
    "7. What specific claims or achievements can be extracted?\n"
    "8. Confidence (0.0-1.0) in your classification.\n\n"
    "Respond ONLY with valid JSON matching this schema:\n"
    "{{\n"
    '  "type": "string",\n'
    '  "dates": [{{"date": "ISO 8601", "context": "string"}}],\n'
    '  "projects": ["string"],\n'
    '  "skills": ["string"],\n'
    '  "people": [{{"name": "string", "role": "string"}}],\n'
    '  "organizations": [{{"name": "string", "role": "string"}}],\n'
    '  "claims": ["string"],\n'
    '  "confidence": 0.0\n'
    "}}"
)

MAX_PREVIEW_CHARS = 8000


@dataclass
class ClassificationResult:
    type: str = "other"
    dates: list[dict] = field(default_factory=list)
    projects: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)
    people: list[dict] = field(default_factory=list)
    organizations: list[dict] = field(default_factory=list)
    claims: list[str] = field(default_factory=list)
    confidence: float = 0.0
    raw_response: str = ""


def classify(text: str, file_type: str, api_key: str | None = None) -> ClassificationResult:
    """Classify extracted text using Gemini. Returns structured classification."""
    key = api_key or os.environ.get("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY not set. Provide it via argument or environment variable.")

    client = genai.Client(api_key=key)

    text_preview = text[:MAX_PREVIEW_CHARS]
    prompt = CLASSIFICATION_PROMPT.format(file_type=file_type, text_preview=text_preview)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.1,
        ),
    )

    raw = response.text or ""
    return _parse_response(raw)


def _parse_response(raw: str) -> ClassificationResult:
    """Parse Gemini's JSON response into a ClassificationResult."""
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return ClassificationResult(raw_response=raw)

    return ClassificationResult(
        type=data.get("type", "other"),
        dates=data.get("dates", []),
        projects=data.get("projects", []),
        skills=data.get("skills", []),
        people=data.get("people", []),
        organizations=data.get("organizations", []),
        claims=data.get("claims", []),
        confidence=float(data.get("confidence", 0.0)),
        raw_response=raw,
    )
