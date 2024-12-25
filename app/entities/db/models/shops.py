import logging

from sqlalchemy import Column, String, Integer

from app.entities.db.init_db import Base
from app.entities.db.models.base import BaseDB

logger = logging.getLogger(__name__)


class Shop(Base):
    __tablename__ = "shop"

    id = Column(Integer, autoincrement="auto", primary_key=True)
    name = Column(String)
    host = Column(String)
    port = Column(Integer)

    def dict(self):
        return {"id": self.id,
                "name": self.name,
                "host": self.host,
                "port": self.port,
                }


class Shops(BaseDB):
    async def new(self, shop: Shop):
        await self._add_obj(shop)

    async def get(self, id: int) -> Shop | None:
        result = await self._get_object(Shop, id)
        return result

    async def update(self, shop: Shop) -> None:
        await self._update_obj(instance=shop, obj=Shop)

    async def delete(self, shop: Shop) -> None:
        await self._delete_obj(instance=shop)

    async def in_(self, id: int) -> Shop | bool:
        result = await self.get(id)
        if type(result) is Shop:
            return result
        return False
