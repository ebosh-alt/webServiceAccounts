import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

Base = declarative_base()

__factory: sessionmaker | None = None

logger = logging.getLogger(__name__)


async def close_database():
    __factory.close_all()


async def create_async_database():
    global __factory
    engine = create_async_engine(settings.database_url)
    if __factory:
        return
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await create_factory()
    await conn.close()


async def create_factory():
    global __factory
    engine = create_async_engine(settings.database_url)
    __factory = sessionmaker(bind=engine, expire_on_commit=True, class_=AsyncSession)


def get_factory():
    global __factory
    return __factory()
