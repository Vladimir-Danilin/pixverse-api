import httpx
import asyncio
import uuid
from src.external_resources.clients.notifier_client import NotifierClient

BASE_API_URL = 'https://app-api.pixverse.ai'
RETRY_STATUS_CODES = {429, 500, 502, 503, 504}
MAX_RETRIES = 3
RETRY_DELAY = 2


class PixverseClient:
    def __init__(self, api_key: str, notifier: NotifierClient):
        self.base_url = BASE_API_URL.rstrip("/")
        self.api_key = api_key
        self.notifier = notifier
        self.client = httpx.AsyncClient(timeout=30)

    async def _retry_request(self, method: str, url: str, **kwargs) -> dict:
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {self.api_key}"
        headers["AI-trace-ID"] = str(uuid.uuid4())
        kwargs["headers"] = headers

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = await self.client.request(method, url, **kwargs)
                if response.status_code not in RETRY_STATUS_CODES:
                    response.raise_for_status()
                    return response.json()
                else:
                    await self.notifier.notify(
                        f"Pixverse {method.upper()} {url} failed with {response.status_code}, attempt {attempt}"
                    )
            except (httpx.RequestError, httpx.HTTPStatusError) as e:
                await self.notifier.notify(f"Pixverse request error: {e}, attempt {attempt}")
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_DELAY)
        raise Exception(f"Pixverse API failed after {MAX_RETRIES} attempts: {url}")

    async def text_to_video(self, prompt: str) -> dict:
        payload = {"prompt": prompt}
        return await self._retry_request("POST", f"{self.base_url}/openapi/v2/video/text/generate", json=payload)

    async def image_to_video(self, prompt: str, image_data: bytes) -> dict:
        files = {"image": ("image.png", image_data, "image/png")}
        data = {"prompt": prompt}
        return await self._retry_request("POST", f"{self.base_url}/openapi/v2/video/img/generate", data=data, files=files)

    async def get_status(self, video_id: str) -> dict:
        return await self._retry_request("GET", f"{self.base_url}/openapi/v2/video/result/{video_id}")
