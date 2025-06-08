import os
from dotenv import load_dotenv

load_dotenv()

PIXVERSE_API_KEY = os.getenv("PIXVERSE_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DATABASE_URL = os.getenv("DATABASE_URL")
