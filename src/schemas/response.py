from pydantic import BaseModel
from typing import Optional


class GenerationResponse(BaseModel):
    generation_id: Optional[str] = None
    message: Optional[str] = None


class StatusResponse(BaseModel):
    status: Optional[str] = None
    video_url: Optional[str] = None
