import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# AI Provider: "gemini" | "groq"
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")
AI_MODEL = os.getenv("AI_MODEL", "")

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Database
DB_PATH = os.getenv("DB_PATH", "data/database/ainglo.db")
TEMP_AUDIO_DIR = os.getenv("TEMP_AUDIO_DIR", "data/temp")
AUDIO_DIR = os.getenv("AUDIO_DIR", "data/audios")
