from google import genai
from google.genai import types
from app.ai.llm.base_provider import BaseAIProvider
from app.config.settings import GEMINI_API_KEY, AI_MODEL
from app.utils.logger import get_logger

logger = get_logger(__name__)

DEFAULT_MODEL = "gemini-2.0-flash"


class GeminiProvider(BaseAIProvider):
    def __init__(self):
        self._client = genai.Client(api_key=GEMINI_API_KEY)
        self._model = AI_MODEL or DEFAULT_MODEL

    def chat(self, messages: list[dict]) -> str:
        system_instruction = None
        contents = []

        for msg in messages:
            role = msg["role"]
            content = msg["content"]

            if role == "system":
                system_instruction = content
            elif role == "user":
                contents.append(
                    types.Content(role="user", parts=[types.Part(text=content)])
                )
            elif role == "assistant":
                contents.append(
                    types.Content(role="model", parts=[types.Part(text=content)])
                )

        config = (
            types.GenerateContentConfig(system_instruction=system_instruction)
            if system_instruction
            else None
        )

        response = self._client.models.generate_content(
            model=self._model,
            contents=contents,
            config=config,
        )
        return response.text

    def is_available(self) -> bool:
        return bool(GEMINI_API_KEY)
