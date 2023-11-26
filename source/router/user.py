from fastapi import APIRouter

from source.service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{user_id}", tags=["user"])
async def read_user(user_id: str):
    return user_service.get_user(user_id)
