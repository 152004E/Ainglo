from abc import ABC, abstractmethod


class BaseAIProvider(ABC):
    @abstractmethod
    def chat(self, messages: list[dict]) -> str:
        ...

    @abstractmethod
    def is_available(self) -> bool:
        ...


def get_provider() -> BaseAIProvider:
    from app.config.settings import AI_PROVIDER

    if AI_PROVIDER == "groq":
        from app.ai.llm.groq_client import GroqProvider
        return GroqProvider()

    from app.ai.llm.gemini_client import GeminiProvider
    return GeminiProvider()
