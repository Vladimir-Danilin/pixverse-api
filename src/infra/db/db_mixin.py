from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config import DATABASE_URL


engine = create_async_engine(url=DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


class DatabaseMixin:
    @staticmethod
    @asynccontextmanager
    async def _cursor():
        async with AsyncSessionLocal() as session:
            yield session
