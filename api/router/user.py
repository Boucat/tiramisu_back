from fastapi import APIRouter

from api.service import user_service

user_router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@user_router.get("/{user_id}", tags=["user"])
async def display_user(user_id: str):
    return user_service.display_user(user_id)
