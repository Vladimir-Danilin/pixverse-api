# app/interfaces/api/routes.py
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.domain.models import TextToVideoRequest, ImageToVideoRequest, GenerationStatusRequest
from app.domain.services import VideoGenerationService
from app.schemas.response import GenerationResponse, StatusResponse

router = APIRouter()


def get_video_generation_service() -> VideoGenerationService:
    from src.config import service  # предполагаем, что service инициализируется в main.py и доступен через config
    return service


@router.post("/text2video", response_model=GenerationResponse)
async def text_to_video(
    request: TextToVideoRequest,
    service: VideoGenerationService = Depends(get_video_generation_service),
):
    try:
        result = await service.generate_from_text(request)
        return GenerationResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/image2video", response_model=GenerationResponse)
async def image_to_video(
    prompt: str,
    image: UploadFile = File(...),
    service: VideoGenerationService = Depends(get_video_generation_service),
):
    try:
        image_bytes = await image.read()
        request = ImageToVideoRequest(prompt=prompt, image_data=image_bytes)
        result = await service.generate_from_image(request)
        return GenerationResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status/{video_id}", response_model=StatusResponse)
async def get_status(
    video_id: str,
    service: VideoGenerationService = Depends(get_video_generation_service),
):
    try:
        request = GenerationStatusRequest(video_id=video_id)
        result = await service.get_status(request)
        return StatusResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
