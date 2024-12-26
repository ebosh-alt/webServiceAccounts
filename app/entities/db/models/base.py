import logging
from typing import Any, Sequence

from sqlalchemy import select, update, Row
from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.db.init_db import get_factory

logger = logging.getLogger(__name__)



class BaseDB:
    @staticmethod  # __table__ = "accounts"
    async def _get_session() -> AsyncSession:
        async with get_factory() as session:
            return session

    async def _add_obj(self, instance):
        async with await self._get_session() as session:
            session.add(instance)
            logger.info(f"add new {instance.__class__.__name__}: {instance.dict()}")
            await session.commit()

    async def _get_object(self, obj, id):
        async with await self._get_session() as session:
            res = await session.get(obj, id)
            return res

    async def _get_objects(self, obj, filters: dict = None):
        async with await self._get_session() as session:
            sql = select(obj)
            if filters is not None:
                for key in filters:
                    sql = sql.where(key == filters[key])
            result = await session.execute(sql)
            return result.scalars().all()

    async def _update_obj(self, obj, instance):
        async with await self._get_session() as session:
            query = update(obj).where(obj.id == instance.id).values(**instance.dict())
            await session.execute(query)
            logger.info(f"update data {instance.__class__.__name__}: {instance.dict()}")
            await session.commit()

    async def _delete_obj(self, instance):
        async with await self._get_session() as session:
            await session.delete(instance)
            logger.info(f"delete {instance.__class__.__name__}: {instance.dict()}")
            await session.commit()

    async def _get_attributes(self, obj, attribute: str) -> Sequence[Row[tuple[Any, ...] | Any]]:
        # получение всех значений конкретного атрибута сущности
        async with await self._get_session() as session:
            sql = select(obj).column(attribute)
            result = await session.execute(sql)
            return result.all()

    async def _in(self, obj, attribute, values: list):
        async with await self._get_session() as session:
            sql = select(obj).where(attribute.in_(values))
            result = await session.execute(sql)
            return result.scalars().all()

    async def _update_all_values(self, obj, attribute, value):
        async with await self._get_session() as session:
            query = update(obj).values({attribute: value})
            await session.execute(query)
            await session.commit()

    async def _bulk_add(self, instances: list[Any]):
        if not instances:
            logger.info("Empty list provided for bulk add")
            return False

        async with await self._get_session() as session:
            session.add_all(instances)
            logger.info(f"Adding {len(instances)} {instances[0].__class__.__name__} to the database")
            await session.commit()
            return True

    async def _exist(self, obj, filters: dict = None) -> bool:
        async with await self._get_session() as session:
            sql = select(obj)
            logger.info(sql)

            if filters is not None:
                # for key, value in filters.items():
                for key in filters:
                    sql = sql.where(key == filters[key])
                    result = await session.execute(sql)
            return result.scalars().first() is not None

