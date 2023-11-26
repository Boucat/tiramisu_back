from fastapi import APIRouter, Depends

from source.dependencies import get_query_token
from source.service import review_tiramisu_service

router = APIRouter(
    prefix="/review_tiramisu",
    tags=["review_tiramisu"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_reviews():
    return review_tiramisu_service.get_all_reviews()


@router.get("/{user_id}")
async def read_reviews_by_user_id():
    return review_tiramisu_service.get_all_reviews_by_user_id()


@router.get("/{restaurant_id}")
async def read_reviews_by_restaurant_id():
    return review_tiramisu_service.get_all_reviews_by_restaurant_id()


@router.post(
    "/",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
    dependencies=[Depends(get_query_token)],
)
async def create_review():
    return review_tiramisu_service.create_review()