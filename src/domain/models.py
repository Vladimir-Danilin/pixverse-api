from pydantic import BaseModel


class TextToVideo(BaseModel):
    prompt: str


class ImageToVideo(BaseModel):
    prompt: str
    image_data: bytes


class GenerationStatus(BaseModel):
    video_id: str
