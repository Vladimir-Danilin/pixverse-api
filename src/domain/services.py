from src.domain.models import TextToVideoRequest, ImageToVideoRequest, GenerationStatusRequest
from src.application.commands import GenerateTextToVideoCommand, GenerateImageToVideoCommand
from src.application.queries import GetGenerationStatusQuery


class VideoGenerationService:
    def __init__(
        self,
        text_to_video_cmd: GenerateTextToVideoCommand,
        image_to_video_cmd: GenerateImageToVideoCommand,
        status_query: GetGenerationStatusQuery,
    ):
        self.text_to_video_cmd = text_to_video_cmd
        self.image_to_video_cmd = image_to_video_cmd
        self.status_query = status_query

    async def generate_from_text(self, request: TextToVideoRequest) -> dict:
        return await self.text_to_video_cmd.execute(request.prompt)

    async def generate_from_image(self, request: ImageToVideoRequest) -> dict:
        return await self.image_to_video_cmd.execute(request.prompt, request.image_data)

    async def get_status(self, request: GenerationStatusRequest) -> dict:
        return await self.status_query.execute(request.video_id)
