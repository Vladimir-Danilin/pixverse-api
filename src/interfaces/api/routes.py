from fastapi import APIRouter, HTTPException, Request, Depends, UploadFile, File
from src.domain.services import VideoGenerationService
from src.schemas.request import TextToVideoRequest, ImageToVideoRequest, GenerationStatusRequest
from src.schemas.response import GenerationResponse, StatusResponse


router = APIRouter()


def get_video_generation_service(request: Request) -> VideoGenerationService:
    return request.app.state.video_generation_service


@router.post("/text2video", response_model=GenerationResponse)
async def text_to_video(
    request: TextToVideoRequest = Depends(),
    service: VideoGenerationService = Depends(get_video_generation_service)
):
    result = await service.generate_from_text(request)
    return GenerationResponse(**result)


@router.post("/image2video", response_model=GenerationResponse)
async def image_to_video(
    request: ImageToVideoRequest = Depends(),
    image: UploadFile = File(..., description="Изображения для генерации видео, не должно превышать 20MB и разрешение 4000х4000"),
    service: VideoGenerationService = Depends(get_video_generation_service)
):
    try:
        result = await service.generate_from_image(request.model_dump(), image)
        return GenerationResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_status_generate/{video_id}", response_model=StatusResponse)
async def get_status(
    request: GenerationStatusRequest = Depends(),
    service: VideoGenerationService = Depends(get_video_generation_service)
):
    try:
        result = await service.get_status(request)
        return StatusResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
