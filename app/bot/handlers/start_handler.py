from telegram import Update
from telegram.ext import ContextTypes
from app.utils.logger import get_logger

logger = get_logger(__name__)


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    logger.info(f"New user: {user.id} - {user.first_name}")

    await update.message.reply_text(
        f"¡Hola {user.first_name}! 👋 Soy *Ainglo*, tu asistente de inglés.\n\n"
        "Puedo ayudarte a:\n"
        "• Corregir tu inglés escrito\n"
        "• Practicar conversación en inglés\n"
        "• Explicarte errores comunes\n\n"
        "Escríbeme en inglés y te ayudo a mejorar. ¡Let's go! 🚀\n\n"
        "_Tip: escribe /reset para reiniciar la conversación._",
        parse_mode="Markdown",
    )
