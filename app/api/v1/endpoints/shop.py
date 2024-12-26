from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse

from app.entities.db.init_db import logger
from app.entities.db.models import Shop
from app.entities.db.models import shops
from app.entities.schemas.Shop import Shop as ShopSchema
from app.services.validate import AuthService

router = APIRouter(prefix="/api/shop",
                   tags=["Магазины"])


@router.get("/getAll", summary="Получения списка всех магазинов")
async def list_shop(auth_key: str = Header(..., alias="auth_key")):
    if not AuthService.auth(auth_key):
        return JSONResponse(
            status_code=400,
            content={"message": {"shops": [], "status": "Auth key is invalid"}},
        )

    return JSONResponse(status_code=200,
                        content={"message": {"shops": [], "status": "List of shops"}}
                        )


@router.post("/create", summary="Создание нового магазина")
async def create_shop(auth_key: str = Header(..., alias="auth_key"), shop: ShopSchema = None):
    logger.info(auth_key)
    logger.info(shop)
    if not AuthService.auth(auth_key):
        return JSONResponse(status_code=400, content={"message": {"status": "Auth key is invalid"}})
    if await shops.exist(shop.name):
        return JSONResponse(status_code=400,
                            content={"message": {"status": "A shop with that name already exists"}})
    shop_db = Shop()
    shop_db.name = shop.name
    shop_db.host = shop.host
    shop_db.port = shop.port
    await shops.new(shop_db)
    return JSONResponse(status_code=200,
                        content={"message": "created new shop"}
                        )
