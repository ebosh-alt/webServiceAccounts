import logging

import aiohttp

from app.entities.schemas.Catalog import Catalog, Response

logger = logging.getLogger(__name__)


class AccountService:
    async def get_catalog(self, host: str, port: int, prefix: str) -> Catalog | str:
        url = f"{host}:{port}{prefix}"
        result = await self.__get(url)

        if result.message.status == "success":
            accounts = result.message.catalog
            logger.info(accounts)
            return Catalog(**{"accounts": accounts})
        else:

            return result.message

    @staticmethod
    async def __get(url) -> Response:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            # Выполняем GET-запрос
            response = await session.get(url=url)
            # Проверяем статус ответа
            if response.status == 200:
                logger.info(f"Successfully get response from {url}, status: {response.status}")
            else:
                logger.info(f"Error in response from {url}, status: {response.status}")

            # Читаем данные JSON из ответа
            data = await response.json()
            await session.close()
        return Response(**data)
