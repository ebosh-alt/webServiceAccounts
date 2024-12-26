from fastapi import APIRouter, Header

from app.entities.db.models import shops
from app.entities.schemas.Catalog import Response, Catalog
from app.services.Account import AccountService
from app.services.validate import AuthService

router = APIRouter(prefix='/api/catalog', tags=['Каталог'])


@router.get("/getByName/{name_shop}", summary="Получение каталога магазина")
async def get_catalog(auth_key: str = Header(..., alias="auth_key"), name_shop: str = None):
    if not AuthService.auth(auth_key):
        return Response(**{"message": {"catalog": [], "status": "error", "detail": "Auth key is invalid"}})

    shop = await shops.get_by_name(name_shop)
    if not shop:
        return Response(**{"message": {"catalog": [], "status": "error", "detail": f"{name_shop} not found"}})

    data = await AccountService().get_catalog(shop.host, shop.port, "/api/catalog/getCatalog")
    if data is not Catalog:
        return Response(**{"message": {"catalog": [], "status": "error", "detail": data.message.status}})
    else:
        return Response(
            **{"message": {"catalog": data.accounts, "status": "success", "detail": "Complete get catalog"}})
