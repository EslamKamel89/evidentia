from collections.abc import AsyncIterator
from typing import Annotated, cast

from fastapi import Depends, Request
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


def get_redis(request: Request) -> Redis:
    return cast(Redis, request.state.redis)


def get_session_factory(
    request: Request,
) -> async_sessionmaker[AsyncSession]:
    return cast(
        async_sessionmaker[AsyncSession],
        request.state.session_factory,
    )


async def get_db_session(
    factory: Annotated[
        async_sessionmaker[AsyncSession],
        Depends(get_session_factory),
    ],
) -> AsyncIterator[AsyncSession]:
    async with factory() as session:
        yield session
