from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_catalog(name: str):
    return {"message": f"User {name} created"}
