import logging

from pydantic_settings import BaseSettings

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    database_url: str
    auth_key: str

    class Config:
        env_file = ".env"


settings = Settings()
