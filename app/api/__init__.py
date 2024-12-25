from fastapi import APIRouter

from .v1.endpoints.catalog import router as router_catalog
from .v1.endpoints.shop import router as router_shop

routers = APIRouter()

routers.include_router(router_catalog)
routers.include_router(router_shop)
