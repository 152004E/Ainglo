import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    raise ValueError(
        "TELEGRAM_TOKEN no configurado"
    )

# AI Provider
AI_PROVIDER = os.getenv(
    "AI_PROVIDER",
    "gemini"
)

AI_MODEL = os.getenv(
    "AI_MODEL",
    "gemini-3.1-flash-lite"
)

# API Keys
GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

# Database
DB_PATH = os.getenv(
    "DB_PATH",
    "data/database/ainglo.db"
)

# Audio
TEMP_AUDIO_DIR = os.getenv(
    "TEMP_AUDIO_DIR",
    "data/temp"
)

AUDIO_DIR = os.getenv(
    "AUDIO_DIR",
    "data/audios"
)