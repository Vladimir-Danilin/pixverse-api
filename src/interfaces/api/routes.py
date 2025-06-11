from fastapi import APIRouter, Request, Depends, UploadFile, File

from src.domain.models import User
from src.domain.services import VideoGenerationService
from src.infra.db.repository import UsersRepository
from src.schemas.request import TextToVideoRequest, ImageToVideoRequest, GenerationStatusRequest
from src.schemas.response import GenerationResponse, StatusResponse


router = APIRouter()


def get_video_generation_service(request: Request) -> VideoGenerationService:
    return request.app.state.video_generation_service


def get_users_repository(request: Request) -> UsersRepository:
    return request.app.state.users_repository


@router.post("/text2video", response_model=GenerationResponse)
async def text_to_video(
    request: TextToVideoRequest = Depends(),
    service: VideoGenerationService = Depends(get_video_generation_service),
    repository: UsersRepository = Depends(get_users_repository)
):
    await repository.save_user(User(app_bundle_id=request.app_bundle_id, apphud_user_id=request.apphud_user_id))
    result = await service.generate_from_text(request)
    return GenerationResponse(**result)


@router.post("/image2video", response_model=GenerationResponse)
async def image_to_video(
    request: ImageToVideoRequest = Depends(),
    image: UploadFile = File(..., description="Изображения для генерации видео, не должно превышать 20MB и разрешение 4000х4000. Поддерживаемые форматы: *.png, *.webp, *.jpeg, *.jpg"),
    service: VideoGenerationService = Depends(get_video_generation_service),
    repository: UsersRepository = Depends(get_users_repository)
):
    await repository.save_user(User(app_bundle_id=request.app_bundle_id, apphud_user_id=request.apphud_user_id))
    result = await service.generate_from_image(request.model_dump(), image)
    return GenerationResponse(**result)


@router.get("/get_status_generate/{video_id}", response_model=StatusResponse)
async def get_status(
    request: GenerationStatusRequest = Depends(),
    service: VideoGenerationService = Depends(get_video_generation_service),
    repository: UsersRepository = Depends(get_users_repository)
):
    await repository.save_user(User(app_bundle_id=request.app_bundle_id, apphud_user_id=request.apphud_user_id))
    result = await service.get_status(request)
    return StatusResponse(**result)
