import asyncio
import logging

from fastapi import FastAPI

from app.api import routers
from app.core.events import lifespan
from app.entities.db.init_db import create_async_database

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-3s [%(asctime)s] - %(message)s",
    filemode="w",
    encoding="utf-8",
)


def get_application() -> FastAPI:
    application = FastAPI(
        lifespan=lifespan,
        title="API",
        description="Получение данных магазинов",
    )
    application.include_router(routers)

    return application


app = get_application()
# asyncio.run(create_async_database())
