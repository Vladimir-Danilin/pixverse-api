from pydantic import BaseModel, Field


class TextToVideoRequest(BaseModel):
    app_bundle_id: str = Field(...)
    apphud_user_id: str = Field(...)
    prompt: str = Field(..., min_length=1, max_length=2048, description="Промпт который передаётся модели для генерации изображения")


class ImageToVideoRequest(BaseModel):
    app_bundle_id: str = Field(...)
    apphud_user_id: str = Field(...)
    prompt: str = Field(..., min_length=1, max_length=2048, description="Промпт который передаётся модели для генерации изображения")
    image_data: bytes = Field(..., description="Изображение, на основе которого будет сгенерировано видео"),


class GenerationStatusRequest(BaseModel):
    app_bundle_id: str = Field(...)
    apphud_user_id: str = Field(...)
    video_id: str = Field(..., description="ID видео, полученное при генерации")
