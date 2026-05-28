from telegram import Update
from telegram.ext import ContextTypes

from app.services.conversation_service import get_response
from app.utils.logger import get_logger

logger = get_logger(__name__)


async def message_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    try:
        user_id = update.effective_user.id
        text = update.message.text

        logger.info(f"Message from {user_id}: {text[:80]}")

        await update.message.chat.send_action("typing")

        response = get_response(user_id, text)

        await update.message.reply_text(response)

    except Exception as e:
        logger.error(f"Message handler error: {e}")

        await update.message.reply_text(
            "Sorry, something went wrong."
        )