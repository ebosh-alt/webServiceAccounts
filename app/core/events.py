import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.entities.db.init_db import create_async_database, close_database

logger = logging.getLogger(__name__)


async def create_start_app_handler():
    """Инициализация базы данных."""
    logger.info("Инициализация базы данных...")
    await create_async_database()
    logging.info("База данных успешно инициализирована.")


async def shutdown_app_handler():
    logging.info("Закрытие соединений с базой данных...")
    await close_database()
    logging.info("Соединения успешно закрыты.")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    logging.info("FastAPI стартует...")
    await create_start_app_handler()
    yield
    await shutdown_app_handler()
    logging.info("FastAPI завершает работу...")
