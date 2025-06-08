from fastapi import FastAPI
from src.config import PIXVERSE_API_KEY, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from src.external_resources.clients.notifier_client import NotifierClient
from src.external_resources.clients.pixverse_client import PixverseClient
from src.interfaces.api.routes import router as api_router

app = FastAPI()

notifier = NotifierClient(token=TELEGRAM_TOKEN, chat_id=TELEGRAM_CHAT_ID)
pixverse_client = PixverseClient(api_key=PIXVERSE_API_KEY, notifier=notifier)

app.include_router(api_router)


@app.get("/ping")
def ping():
    return {"status": "ok"}
