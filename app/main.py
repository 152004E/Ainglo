import os
from app.database.connection import init_db
from app.bot.telegram_bot import run_bot
from app.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    logger.info("Initializing Ainglo...")

    for directory in ["data/database", "data/temp", "data/audios"]:
        os.makedirs(directory, exist_ok=True)

    init_db()
    logger.info("Database initialized.")

    run_bot()


if __name__ == "__main__":
    main()
