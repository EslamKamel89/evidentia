from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class CLISettings(BaseSettings):
    app_url: str = "http://127.0.0.1:8000"
    timeout: float = Field(gt=0, default=5)
    model_config = SettingsConfigDict(
        env_prefix="EVIDENTIA_",
        extra="ignore",
        frozen=True,
    )


@lru_cache(maxsize=1)
def get_settings() -> CLISettings:
    return CLISettings()
