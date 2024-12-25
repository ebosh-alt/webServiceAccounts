import logging

from fastapi import FastAPI

from app.api import routers
from app.core.events import lifespan

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

    # Регистрируем обработчик on_startup
    # application.add_event_handler("startup", create_start_app_handler)
    # application.add_event_handler("shutdown", shutdown_app_handler)

    return application


app = get_application()
