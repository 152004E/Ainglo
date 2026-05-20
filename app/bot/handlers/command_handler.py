from telegram import Update
from telegram.ext import ContextTypes
from app.services.conversation_service import clear_history
from app.utils.logger import get_logger

logger = get_logger(__name__)


async def reset_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    clear_history(user_id)
    logger.info(f"History cleared for user {user_id}")
    await update.message.reply_text(
        "Conversación reiniciada. ¡Empecemos de nuevo! 🔄"
    )


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "*Comandos disponibles:*\n\n"
        "/start — Bienvenida\n"
        "/reset — Reiniciar conversación\n"
        "/help — Ver esta ayuda\n\n"
        "Escríbeme en inglés y te corrijo y ayudo a mejorar. 💪",
        parse_mode="Markdown",
    )
