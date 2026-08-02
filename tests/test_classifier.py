"""Tests for Gemini document classification."""

import json
from unittest.mock import MagicMock, patch

import pytest

from twin.ingestion.classifier import ClassificationResult, _parse_response, classify


class TestParseResponse:
    def test_valid_json(self):
        raw = json.dumps(
            {
                "type": "email_appreciation",
                "dates": [{"date": "2026-07-15", "context": "demo date"}],
                "projects": ["Chitta"],
                "skills": ["knowledge_graphs", "nlp"],
                "people": [{"name": "Sarah Chen", "role": "VP Engineering"}],
                "claims": ["Reduced search time from hours to seconds"],
                "confidence": 0.92,
            }
        )
        result = _parse_response(raw)
        assert result.type == "email_appreciation"
        assert result.confidence == 0.92
        assert "Chitta" in result.projects
        assert len(result.people) == 1
        assert result.people[0]["name"] == "Sarah Chen"
        assert "knowledge_graphs" in result.skills

    def test_partial_json(self):
        raw = json.dumps({"type": "project_doc", "confidence": 0.5})
        result = _parse_response(raw)
        assert result.type == "project_doc"
        assert result.confidence == 0.5
        assert result.projects == []
        assert result.claims == []

    def test_invalid_json_returns_empty_result(self):
        result = _parse_response("not json at all")
        assert result.type == "other"
        assert result.confidence == 0.0
        assert result.raw_response == "not json at all"

    def test_empty_response(self):
        result = _parse_response("{}")
        assert result.type == "other"
        assert result.confidence == 0.0


class TestClassify:
    def test_raises_without_api_key(self):
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="GEMINI_API_KEY"):
                classify("some text", "md", api_key=None)

    def test_calls_gemini_and_returns_result(self):
        mock_response = MagicMock()
        mock_response.text = json.dumps(
            {
                "type": "project_doc",
                "dates": [],
                "projects": ["Twin"],
                "skills": ["python"],
                "people": [],
                "claims": ["Built a knowledge graph"],
                "confidence": 0.85,
            }
        )

        with patch("twin.ingestion.classifier.genai.Client") as mock_client_cls:
            mock_client = MagicMock()
            mock_client.models.generate_content.return_value = mock_response
            mock_client_cls.return_value = mock_client

            result = classify("Some project documentation text.", "md", api_key="fake-key")

        assert result.type == "project_doc"
        assert result.confidence == 0.85
        assert "Twin" in result.projects
        mock_client_cls.assert_called_once_with(api_key="fake-key")
        mock_client.models.generate_content.assert_called_once()

    def test_truncates_long_text(self):
        long_text = "x" * 20000

        mock_response = MagicMock()
        mock_response.text = json.dumps({"type": "other", "confidence": 0.3})

        with patch("twin.ingestion.classifier.genai.Client") as mock_client_cls:
            mock_client = MagicMock()
            mock_client.models.generate_content.return_value = mock_response
            mock_client_cls.return_value = mock_client

            classify(long_text, "txt", api_key="fake-key")

            call_kwargs = mock_client.models.generate_content.call_args
            prompt = call_kwargs.kwargs.get("contents") or call_kwargs[1].get("contents")
            assert len(prompt) < 20000


class TestClassificationResult:
    def test_defaults(self):
        r = ClassificationResult()
        assert r.type == "other"
        assert r.confidence == 0.0
        assert r.projects == []
        assert r.raw_response == ""
