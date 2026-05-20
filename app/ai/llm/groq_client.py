from groq import Groq
from app.ai.llm.base_provider import BaseAIProvider
from app.config.settings import GROQ_API_KEY, AI_MODEL
from app.utils.logger import get_logger

logger = get_logger(__name__)

DEFAULT_MODEL = "llama-3.3-70b-versatile"


class GroqProvider(BaseAIProvider):
    def __init__(self):
        self._client = Groq(api_key=GROQ_API_KEY)
        self._model = AI_MODEL or DEFAULT_MODEL

    def chat(self, messages: list[dict]) -> str:
        response = self._client.chat.completions.create(
            model=self._model,
            messages=messages,
        )
        return response.choices[0].message.content

    def is_available(self) -> bool:
        return bool(GROQ_API_KEY)
