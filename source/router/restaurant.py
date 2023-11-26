from fastapi import APIRouter

from source.service import restaurant_service

router = APIRouter(
    prefix="/restaurant",
    tags=["restaurant"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{restaurant_id}", tags=["restaurant"])
async def read_restaurant(restaurant_id: str):
    return restaurant_service.get_restaurant(restaurant_id)
