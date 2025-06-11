from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, Mapped

Base = declarative_base()


class TextToVideo(BaseModel):
    prompt: str


class ImageToVideo(BaseModel):
    prompt: str
    image_data: bytes


class GenerationStatus(BaseModel):
    video_id: str


class User(Base):
    __tablename__ = 'user'

    id: Mapped[UUID] = mapped_column(primary_key=True, index=True, default=uuid4())
    app_bundle_id: Mapped[str]
    apphud_user_id: Mapped[str]
