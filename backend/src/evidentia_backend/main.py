from asyncio import timeout
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Annotated, TypedDict

from evidentia_backend.core.config import get_settings
from evidentia_backend.core.dependencies import get_db_session, get_redis
from fastapi import Depends, FastAPI, HTTPException
from redis.asyncio import Redis
from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


class AppState(TypedDict):
    engine: AsyncEngine
    redis: Redis
    session_factory: async_sessionmaker[AsyncSession]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[AppState]:
    settings = get_settings()

    engine = create_async_engine(
        settings.database_url,
        pool_pre_ping=True,
        connect_args={"timeout": 3},
    )

    redis = Redis.from_url(
        settings.redis_url,
        socket_connect_timeout=2,
        socket_timeout=2,
    )

    session_factory = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    try:
        yield {
            "engine": engine,
            "redis": redis,
            "session_factory": session_factory,
        }
    finally:
        await redis.aclose()
        await engine.dispose()


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        lifespan=lifespan,
    )

    @app.get("/api/v1/health")
    async def health_check() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/api/v1/ready")
    async def readiness_check(
        session: Annotated[
            AsyncSession,
            Depends(get_db_session),
        ],
        redis: Annotated[
            Redis,
            Depends(get_redis),
        ],
    ) -> dict[str, str]:
        try:
            async with timeout(3):
                await session.execute(text("SELECT 1"))
                await redis.ping()

        except Exception as exc:
            raise HTTPException(
                status_code=503,
                detail="Infrastructure unavailable",
            ) from exc

        return {"status": "ready"}

    return app


app = create_app()
