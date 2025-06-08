from src.external_resources.clients.pixverse_client import PixverseClient


class GetGenerationStatusQuery:
    def __init__(self, client: PixverseClient):
        self.client = client

    async def execute(self, generation_id: str) -> dict:
        return await self.client.get_status(generation_id)
