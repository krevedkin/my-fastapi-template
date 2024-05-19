from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from core.config import settings


class DatabaseHelper:

    def __init__(self, url: str, pool_size: int, max_overflow: int):
        self.async_engine = create_async_engine(
            url=url,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_factory = async_sessionmaker(
            self.async_engine,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )

    async def dispose(self) -> None:
        await self.async_engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper(
    url=settings.db.url,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)
