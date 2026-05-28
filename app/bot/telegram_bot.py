from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from app.config.settings import TELEGRAM_TOKEN
from app.bot.handlers.start_handler import start_handler
from app.bot.handlers.message_handler import message_handler
from app.bot.handlers.command_handler import reset_handler, help_handler
from app.utils.logger import get_logger

logger = get_logger(__name__)


def create_bot():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN not set in .env file")

    app = (
    ApplicationBuilder()
    .token(TELEGRAM_TOKEN)
    .connect_timeout(30)
    .read_timeout(30)
    .write_timeout(30)
    .pool_timeout(30)
    .build()
)

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("reset", reset_handler))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    return app


def run_bot():
    logger.info("Starting Ainglo bot...")
    app = create_bot()
    app.run_polling(drop_pending_updates=True)
