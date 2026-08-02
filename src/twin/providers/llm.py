"""LLM provider abstraction with Gemini primary and Ollama fallback."""

import os
from abc import ABC, abstractmethod
from dataclasses import dataclass

import httpx
from google import genai
from google.genai import types


@dataclass
class LLMResponse:
    text: str
    provider: str
    model: str


class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, system: str = "", temperature: float = 0.7) -> LLMResponse: ...


class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str | None = None, model: str = "gemini-2.5-flash"):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY", "")
        self.model = model

    def generate(self, prompt: str, system: str = "", temperature: float = 0.7) -> LLMResponse:
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not configured")

        client = genai.Client(api_key=self.api_key)
        contents = prompt
        config = types.GenerateContentConfig(
            temperature=temperature,
            system_instruction=system if system else None,
        )

        response = client.models.generate_content(
            model=self.model,
            contents=contents,
            config=config,
        )
        return LLMResponse(text=response.text or "", provider="gemini", model=self.model)


class OllamaProvider(LLMProvider):
    def __init__(
        self,
        base_url: str | None = None,
        model: str = "gemma3",
    ):
        self.base_url = base_url or os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
        self.model = model

    def generate(self, prompt: str, system: str = "", temperature: float = 0.7) -> LLMResponse:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "system": system,
            "stream": False,
            "options": {"temperature": temperature},
        }
        response = httpx.post(f"{self.base_url}/api/generate", json=payload, timeout=120.0)
        response.raise_for_status()
        data = response.json()
        return LLMResponse(text=data.get("response", ""), provider="ollama", model=self.model)


class ProviderRouter(LLMProvider):
    """Routes to primary provider, falls back to secondary on failure."""

    def __init__(
        self,
        primary: LLMProvider | None = None,
        fallback: LLMProvider | None = None,
    ):
        self.primary = primary or GeminiProvider()
        self.fallback = fallback or OllamaProvider()

    def generate(self, prompt: str, system: str = "", temperature: float = 0.7) -> LLMResponse:
        try:
            return self.primary.generate(prompt, system, temperature)
        except Exception:
            return self.fallback.generate(prompt, system, temperature)
