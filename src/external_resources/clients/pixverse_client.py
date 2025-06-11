import io
import json

import httpx
import asyncio
import uuid

from src.external_resources.clients.notifier_client import NotifierClient
from src.external_resources.exceptions.pixverse_exceptions import ExternalPixverseTimeoutError, PIXVERSE_ERROR_MAP, \
    ExternalPixverseError, API_ERROR_MAP


BASE_API_URL = 'https://app-api.pixverse.ai'
BOUNDARY = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
MAX_RETRIES = 3
RETRY_DELAY = 5

ASPECT_RATIO = "16:9"  # 16:9, 4:3, 1:1, 3:4, 9:16
DURATION = 5  # 5 or 8 second. 1080p doesn't support 8 second
PIXVERSE_MODEL = "v3.5"  # v3.5, v4, v4.5
QUALITY = "540p"  # 360p, 540p, 720p, 1080p


PIXVERSE_STATUS_MAP = {
    1: "SUCCESS",
    5: "GENERATING",
    6: "DELETED",
    7: "MODERATION_FAILED",
    8: "GENERATION_FAILED"
}


class PixverseClient:
    def __init__(self, api_key: str, notifier: NotifierClient):
        self.base_url = BASE_API_URL.rstrip("/")
        self.api_key = api_key
        self.notifier = notifier
        self.client = httpx.AsyncClient(timeout=30)

    async def _retry_request(self, method: str, endpoint: str, content_type: str = "application/json", **kwargs) -> dict:
        url = f"{self.base_url}{endpoint}"
        headers = kwargs.pop("headers", {})
        headers["API-KEY"] = self.api_key
        headers["Ai-trace-id"] = str(uuid.uuid4())
        headers["Content-Type"] = content_type
        kwargs["headers"] = headers

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                response = await self.client.request(method, url, **kwargs)
                r = response.json()
                err_code = r.get("ErrCode")
                err_message = r.get("ErrMsg")

                if err_code and err_code != 200:
                    error_class = PIXVERSE_ERROR_MAP.get(err_code, ExternalPixverseError)
                    await self.notifier.endpoint_pixverse_error(
                        error_code=err_code,
                        error_message=err_message,
                        endpoint=endpoint,
                        method=method
                    )
                    raise error_class(
                        endpoint=endpoint,
                        detail=f"{err_code} - {err_message}"
                    )

                return r
            except httpx.HTTPStatusError as e:
                status_code = e.response.status_code
                await self.notifier.server_pixverse_error(error=e, attempt=attempt)

                error_class = API_ERROR_MAP.get(status_code, ExternalPixverseError)

                if status_code in API_ERROR_MAP and attempt < MAX_RETRIES:
                    await asyncio.sleep(RETRY_DELAY)
                    continue

                raise error_class(
                    status_code=status_code,
                    endpoint=url,
                    detail=f"HTTP error {status_code}: {str(e)}"
                )

            except httpx.RequestError as e:
                await self.notifier.server_pixverse_error(error=e, attempt=attempt)
                if attempt < MAX_RETRIES:
                    await asyncio.sleep(RETRY_DELAY)
                    continue

        await self.notifier.server_pixverse_error(error=url, attempt=MAX_RETRIES)
        raise ExternalPixverseTimeoutError(
            endpoint=url,
            detail=f"Max retries exceeded for {url}",
            timeout=self.client.timeout.read
        )

    async def text_to_video(self, prompt: str) -> dict:
        payload = json.dumps({
            "model": PIXVERSE_MODEL,
            "aspect_ratio": ASPECT_RATIO,
            "duration": DURATION,
            "quality": QUALITY,
            "prompt": prompt,
        })
        result = await self._retry_request("POST", "/openapi/v2/video/text/generate", content=payload)
        return {"generation_id": str(result.get("Resp", {}).get("video_id"))}

    async def image_to_video(self, prompt: str, image_data: bytes) -> dict:
        files = {
            "image": ("upload.png", io.BytesIO(image_data), "image/png")
        }
        upload_image_data = await self._retry_request(
            method="POST",
            endpoint="/openapi/v2/image/upload",
            content_type=f"multipart/form-data; boundary={BOUNDARY}",
            files=files)

        payload = json.dumps({
            "duration": DURATION,
            "model": PIXVERSE_MODEL,
            "aspect_ratio": ASPECT_RATIO,
            "quality": QUALITY,
            "img_id": upload_image_data.get("Resp", {}).get("img_id"),
            "prompt": prompt,
        })
        result = await self._retry_request(method="POST", endpoint="/openapi/v2/video/img/generate", content=payload)
        return {"generation_id": str(result.get("Resp", {}).get("video_id"))}

    async def get_status(self, video_id: str) -> dict:
        result = await self._retry_request("GET", f"/openapi/v2/video/result/{video_id}")
        resp = result.get("Resp", {})
        url = resp.get("url")
        status_code = resp.get("status")
        status = PIXVERSE_STATUS_MAP.get(status_code, f"Неизвестный статус: {status_code}")
        return {"video_url": url, "status": status} if url else {"status": status}


