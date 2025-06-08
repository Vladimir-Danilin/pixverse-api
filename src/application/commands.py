from src.external_resources.clients.pixverse_client import PixverseClient


class GenerateTextToVideoCommand:
    def __init__(self, client: PixverseClient):
        self.client = client

    async def execute(self, prompt: str) -> dict:
        return await self.client.text_to_video(prompt)


class GenerateImageToVideoCommand:
    def __init__(self, client: PixverseClient):
        self.client = client

    async def execute(self, prompt: str, image_data: bytes) -> dict:
        return await self.client.image_to_video(prompt, image_data)