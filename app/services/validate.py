import logging

from app.core.config import settings

logger = logging.getLogger(__name__)


class AuthService:
    @staticmethod
    def auth(auth_key: str):
        if auth_key == settings.auth_key:
            return True
        return False
