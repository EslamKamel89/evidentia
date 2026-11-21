from pydantic import BaseModel, ConfigDict


class APIResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")


class HealthResponse(APIResponse):
    status: str


class InfoResponse(APIResponse):
    name: str
    version: str
