from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Evidentia API"
    database_url: str
    redis_url: str = "redis://localhost:6379/0"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        frozen=True,
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()  # pyright: ignore[reportCallIssue]
