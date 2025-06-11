from fastapi import HTTPException, status
from typing import Optional, Any, Type


class ExternalPixverseError(HTTPException):
    def __init__(
            self,
            status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
            api_name: str = 'pixverse',
            endpoint: str = None,
            detail: str = None,
            headers: Optional[dict[str, Any]] = None,
    ):
        super().__init__(
            status_code=status_code,
            detail=detail,
            headers=headers or {}
        )
        self.api_name = api_name
        self.endpoint = endpoint

    def __str__(self):
        return f"[{self.api_name}] {self.status_code} - {self.detail} (Endpoint: {self.endpoint})"


class ExternalPixverseAPIKeyEmpty(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = "API key empty"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseEmptyParameter(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseInvalidAccount(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseInvalidTypeOrValue(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseInvalidParams(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixversePromptLenghtLimit(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseInvalidImageId(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseRequestDataNotFound(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseUserPermissionDenied(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixversePermissionDenied(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseIncorrectImageSize(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseFailedFetchImageInfo(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseInvalidImageFormat(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseInvalidImageWidthOrHeight(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseImageUploadFailed(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseInvalidImagePath(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseGenerationLimit(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseContentModerationFailure(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseMountlyLimit(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixversePromptModerationFailure(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseContentDelete(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseHighLoad(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseTemplateNotActive(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseInsufficientBalance(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseMySQLError(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseUnknownError(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, detail: str = None):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            api_name=api_name,
            endpoint=endpoint
        )


class ExternalPixverseRateLimitError(ExternalPixverseError):
    def __init__(self, api_name: str, endpoint: str, reset_time: Optional[int] = None):
        headers = {}
        if reset_time:
            headers["X-RateLimit-Reset"] = str(reset_time)

        super().__init__(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="API rate limit exceeded",
            api_name=api_name,
            endpoint=endpoint,
            headers=headers
        )


class ExternalPixverseInvalidResponseError(ExternalPixverseError):
    def __init__(self, api_name: str = "pixverse", endpoint: str = None, validation_errors: list = None):
        super().__init__(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Invalid API response format",
            api_name=api_name,
            endpoint=endpoint,
            headers={"X-Validation-Errors": str(validation_errors)}
        )


class ExternalPixverseTimeoutError(ExternalPixverseError):
    def __init__(self, api_name: str = 'pixverse', endpoint: str = None, detail: str = None, timeout: float = None):
        message = detail if detail else f"Timeout after {timeout} seconds"
        super().__init__(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail=message,
            api_name=api_name,
            endpoint=endpoint
        )


PIXVERSE_ERROR_MAP: dict[int, Type[ExternalPixverseError]] = {
    10004: ExternalPixverseAPIKeyEmpty,
    400011: ExternalPixverseEmptyParameter,
    400012: ExternalPixverseInvalidAccount,
    400013: ExternalPixverseInvalidTypeOrValue,
    400017: ExternalPixverseInvalidParams,
    400018: ExternalPixversePromptLenghtLimit,
    400019: ExternalPixversePromptLenghtLimit,
    400032: ExternalPixverseInvalidImageId,
    500008: ExternalPixverseRequestDataNotFound,
    500020: ExternalPixverseUserPermissionDenied,
    500030: ExternalPixverseIncorrectImageSize,
    500031: ExternalPixverseFailedFetchImageInfo,
    500032: ExternalPixverseInvalidImageFormat,
    500033: ExternalPixverseInvalidImageWidthOrHeight,
    500041: ExternalPixverseImageUploadFailed,
    500042: ExternalPixverseInvalidImagePath,
    500044: ExternalPixverseGenerationLimit,
    500054: ExternalPixverseContentModerationFailure,
    500060: ExternalPixverseMountlyLimit,
    500063: ExternalPixversePromptModerationFailure,
    500064: ExternalPixverseContentDelete,
    500069: ExternalPixverseHighLoad,
    500070: ExternalPixverseTemplateNotActive,
    500090: ExternalPixverseInsufficientBalance,
    500100: ExternalPixverseMySQLError,
    99999: ExternalPixverseUnknownError,
    500: ExternalPixverseError,
    None: ExternalPixverseError,
}

API_ERROR_MAP: dict[int, Type[ExternalPixverseError]] = {
    429: ExternalPixverseRateLimitError,
    502: ExternalPixverseInvalidResponseError,
    None: ExternalPixverseError,
}
