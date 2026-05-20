from app.ai.llm.base_provider import get_provider
from app.ai.llm.prompts import build_system_message
from app.config.constants import MAX_HISTORY_MESSAGES
from app.utils.logger import get_logger

logger = get_logger(__name__)

_provider = get_provider()
_histories: dict[int, list[dict]] = {}


def get_response(user_id: int, user_message: str) -> str:
    if user_id not in _histories:
        _histories[user_id] = [build_system_message()]

    _histories[user_id].append({"role": "user", "content": user_message})

    if len(_histories[user_id]) > MAX_HISTORY_MESSAGES + 1:
        _histories[user_id] = (
            [_histories[user_id][0]] + _histories[user_id][-MAX_HISTORY_MESSAGES:]
        )

    try:
        response = _provider.chat(_histories[user_id])
        _histories[user_id].append({"role": "assistant", "content": response})
        return response
    except Exception as e:
        logger.error(f"Conversation error for user {user_id}: {e}")
        return "Lo siento, hubo un error al procesar tu mensaje. Intenta de nuevo. 🙏"


def clear_history(user_id: int):
    _histories.pop(user_id, None)
