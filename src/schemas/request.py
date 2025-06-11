from fastapi import Query
from fastapi.params import Path
from pydantic import BaseModel, Field


class TextToVideoRequest(BaseModel):
    app_bundle_id: str = Field(...)
    apphud_user_id: str = Field(...)
    prompt: str = Field(Query(description="Промпт, передаётся модели для генерации видео"), min_length=1, max_length=2048)


class ImageToVideoRequest(BaseModel):
    app_bundle_id: str = Field(...)
    apphud_user_id: str = Field(...)
    prompt: str = Field(Query(description="Промпт, передаётся модели для генерации видео"), min_length=1, max_length=2048)


class GenerationStatusRequest(BaseModel):
    app_bundle_id: str = Field(...)
    apphud_user_id: str = Field(...)
    video_id: str = Field(Path(..., description="ID видео, полученное при запросе на его генерации"), description="ID видео, полученное при запросе на его генерации")
