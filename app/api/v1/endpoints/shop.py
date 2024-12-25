from fastapi import APIRouter, Header, HTTPException

from app.entities.db.models import Shop
from app.entities.db.models import shops
from app.entities.schemas.Shop import Shop as ShopSchema
from app.services.validate import AuthService

router = APIRouter(prefix="/shop",
                   tags=["Магазины"])


@router.get("/getAll", summary="Получения списка всех магазинов")
async def list_shop(auth_key: str = Header(..., alias="auth_key")):
    if not AuthService.auth(auth_key):
        raise HTTPException(status_code=401, detail="Invalid AUTH Key")

    return {"message": "List of shops"}


@router.post("/create", summary="Создание нового магазина")
async def create_shop(auth_key: str = Header(..., alias="auth_key"), shop: ShopSchema = None):
    if not AuthService.auth(auth_key):
        raise HTTPException(status_code=401, detail="Invalid AUTH Key")
    shop_db = Shop()
    shop_db.name = shop.name
    shop_db.host = shop.host
    shop_db.port = shop.port
    await shops.new(shop_db)
    return {"status": "success",
            "message": "created new shop"}
