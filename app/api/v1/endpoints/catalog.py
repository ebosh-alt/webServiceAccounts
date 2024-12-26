from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse

from app.entities.db.init_db import logger
from app.entities.db.models import shops
from app.entities.schemas.Catalog import Response
from app.services.Account import AccountService
from app.services.validate import AuthService

router = APIRouter(prefix='/api/catalog', tags=['Каталог'])


@router.get("/getByName/{name_shop}", summary="Получение каталога магазина")
async def get_catalog(auth_key: str = Header(..., alias="auth_key"), name_shop: str = None):
    if not AuthService.auth(auth_key):
        return JSONResponse(
            status_code=404,
            content={"message": {"catalog": [], "status": "Auth key is invalid"}},
        )
    shop = await shops.get_by_name(name_shop)
    if not shop:
        return JSONResponse(
            status_code=404,
            content={"message": {"catalog": [], "status": f"{name_shop} not found"}},
        )
    logger.info(shop.dict())
    catalog = await AccountService().get_catalog(shop.host, shop.port, "/api/catalog/getCatalog")
    return Response(**{"status_code": 200, "message": {"catalog": catalog.accounts, "status": "success"}})

    # return {
    #     "status_code": 200,
    #     "content": {"message": {accounts, "status": "success"}},
    # }
