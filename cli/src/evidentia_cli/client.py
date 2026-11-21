import httpx
from evidentia_cli.schemas import HealthResponse, InfoResponse
from pydantic import BaseModel, ValidationError


class APIClientError(Exception):
    """Base exception for API communication failures."""


class APIConnectionError(APIClientError):
    """The API could not be reached."""


class APIRequestError(APIClientError):
    """The API returned an unsuccessful response."""


class APIContractError(APIClientError):
    """The API returned an unexpected response structure."""


class EvidentiaClient:
    def __init__(
        self,
        base_url: str,
        timeout: float = 5.0,
        transport: httpx.BaseTransport | None = None,
    ):
        self._client = httpx.Client(
            base_url=base_url, timeout=timeout, transport=transport
        )

    def __enter__(self) -> "EvidentiaClient":
        return self

    def __exit__(self, *args) -> None:
        self._client.close()

    def _get[T: BaseModel](self, path: str, response_model: type[T]) -> T:
        try:
            response = self._client.get(path)
            response.raise_for_status()
        except httpx.RequestError as exc:
            raise APIConnectionError(str(exc)) from exc
        except httpx.HTTPStatusError as exc:
            raise APIRequestError(str(exc)) from exc
        try:
            return response_model.model_validate(response.json())
        except (ValueError, ValidationError) as exc:
            raise APIContractError("API returned an invalid response") from exc

    def health(self) -> HealthResponse:
        return self._get("/api/v1/health", HealthResponse)

    def info(self) -> InfoResponse:
        return self._get("/api/v1/info", InfoResponse)
