from pydantic import BaseModel


class TextToVideoRequest(BaseModel):
    app_bundle_id: str
    apphud_user_id: str
    prompt: str


class ImageToVideoRequest(BaseModel):
    app_bundle_id: str
    apphud_user_id: str
    prompt: str


class StatusRequest(BaseModel):
    app_bundle_id: str
    apphud_user_id: str
    video_id: str
