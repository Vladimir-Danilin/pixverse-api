from pydantic import BaseModel


class TextToVideoRequest(BaseModel):
    prompt: str


class ImageToVideoRequest(BaseModel):
    prompt: str
    image_data: bytes


class GenerationStatusRequest(BaseModel):
    video_id: str
