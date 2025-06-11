from pydantic import BaseModel, Field
from typing import Optional


class GenerationResponse(BaseModel):
    generation_id: Optional[str] = Field(default=None)


class StatusResponse(BaseModel):
    status: Optional[str] = Field(default=None)
    video_url: Optional[str] = Field(default=None)
