from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from src.config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, PIXVERSE_API_KEY
from src.application.commands import GenerateTextToVideoCommand, GenerateImageToVideoCommand
from src.application.queries import GetGenerationStatusQuery
from src.external_resources.clients.notifier_client import NotifierClient
from src.external_resources.clients.pixverse_client import PixverseClient
from src.external_resources.exceptions.pixverse_exceptions import ExternalPixverseError
from src.infra.db.repository import UsersRepository
from src.interfaces.api.routes import router
from src.domain.services import VideoGenerationService


@asynccontextmanager
async def app_lifespan(appfastapi: FastAPI):
    notifier = NotifierClient(
        token=TELEGRAM_TOKEN,
        chat_id=TELEGRAM_CHAT_ID
    )
    pixverse_client = PixverseClient(
        api_key=PIXVERSE_API_KEY,
        notifier=notifier
    )

    text_to_video_cmd = GenerateTextToVideoCommand(pixverse_client)
    image_to_video_cmd = GenerateImageToVideoCommand(pixverse_client)
    status_query = GetGenerationStatusQuery(pixverse_client)

    service = VideoGenerationService(
        text_to_video_cmd=text_to_video_cmd,
        image_to_video_cmd=image_to_video_cmd,
        status_query=status_query
    )

    appfastapi.state.video_generation_service = service
    appfastapi.state.users_repository = UsersRepository()
    appfastapi.state.notifier = notifier
    yield


app = FastAPI(lifespan=app_lifespan)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    route_path = request.url.path
    method = request.method

    notifier: NotifierClient = request.app.state.notifier
    await notifier.invalid_value_error(method=method, route=route_path, error=exc.errors())

    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": exc.errors(),
            "body": exc.body,
            "message": "Данные запроса не прошли валидацию. Проверьте поля."
        },
    )


@app.exception_handler(ExternalPixverseError)
async def handle_external_pixverse_error(request: Request, exc: ExternalPixverseError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "api": exc.api_name,
            "endpoint": exc.endpoint,
        },
        headers=exc.headers,
    )

app.include_router(router)


@app.get("/ping")
def ping():
    return {"status": "success"}


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000)
