"""Tests for LLM provider abstraction."""

from unittest.mock import MagicMock, patch

import pytest

from twin.providers.llm import (
    GeminiProvider,
    LLMResponse,
    OllamaProvider,
    ProviderRouter,
)


class TestGeminiProvider:
    def test_raises_without_api_key(self):
        with patch.dict("os.environ", {}, clear=True):
            provider = GeminiProvider(api_key="")
            with pytest.raises(ValueError, match="GEMINI_API_KEY"):
                provider.generate("hello")

    def test_calls_gemini(self):
        mock_response = MagicMock()
        mock_response.text = "I built knowledge graphs."

        with patch("twin.providers.llm.genai.Client") as mock_client_cls:
            mock_client = MagicMock()
            mock_client.models.generate_content.return_value = mock_response
            mock_client_cls.return_value = mock_client

            provider = GeminiProvider(api_key="fake-key", model="gemini-2.5-flash")
            result = provider.generate("Tell me about yourself", system="Be concise")

        assert result.text == "I built knowledge graphs."
        assert result.provider == "gemini"
        assert result.model == "gemini-2.5-flash"

    def test_passes_temperature(self):
        mock_response = MagicMock()
        mock_response.text = "response"

        with patch("twin.providers.llm.genai.Client") as mock_client_cls:
            mock_client = MagicMock()
            mock_client.models.generate_content.return_value = mock_response
            mock_client_cls.return_value = mock_client

            provider = GeminiProvider(api_key="fake")
            provider.generate("test", temperature=0.2)

            call_kwargs = mock_client.models.generate_content.call_args
            config = call_kwargs.kwargs.get("config") or call_kwargs[1].get("config")
            assert config.temperature == 0.2


class TestOllamaProvider:
    def test_calls_ollama_api(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "Hello from Ollama"}
        mock_response.raise_for_status = MagicMock()

        with patch("twin.providers.llm.httpx.post", return_value=mock_response) as mock_post:
            provider = OllamaProvider(base_url="http://localhost:11434", model="gemma3")
            result = provider.generate("hello", system="sys")

        assert result.text == "Hello from Ollama"
        assert result.provider == "ollama"
        assert result.model == "gemma3"
        mock_post.assert_called_once()
        call_kwargs = mock_post.call_args
        payload = call_kwargs.kwargs.get("json") or call_kwargs[1].get("json")
        assert payload["model"] == "gemma3"
        assert payload["system"] == "sys"


class TestProviderRouter:
    def test_uses_primary_on_success(self):
        primary = MagicMock(spec=GeminiProvider)
        primary.generate.return_value = LLMResponse(
            text="primary", provider="gemini", model="flash"
        )
        fallback = MagicMock(spec=OllamaProvider)

        router = ProviderRouter(primary=primary, fallback=fallback)
        result = router.generate("test")

        assert result.text == "primary"
        fallback.generate.assert_not_called()

    def test_falls_back_on_primary_failure(self):
        primary = MagicMock(spec=GeminiProvider)
        primary.generate.side_effect = Exception("API error")
        fallback = MagicMock(spec=OllamaProvider)
        fallback.generate.return_value = LLMResponse(
            text="fallback", provider="ollama", model="gemma3"
        )

        router = ProviderRouter(primary=primary, fallback=fallback)
        result = router.generate("test")

        assert result.text == "fallback"
        assert result.provider == "ollama"

    def test_propagates_fallback_error(self):
        primary = MagicMock()
        primary.generate.side_effect = Exception("primary down")
        fallback = MagicMock()
        fallback.generate.side_effect = Exception("fallback down")

        router = ProviderRouter(primary=primary, fallback=fallback)
        with pytest.raises(Exception, match="fallback down"):
            router.generate("test")
