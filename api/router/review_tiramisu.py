from fastapi import APIRouter, Depends

from api.dependencies import check_user_token

review_tiramisu_router = APIRouter(
    prefix='/review_tiramisu',
    tags=['review_tiramisu'],
    responses={404: {'description': 'Not found'}},
)


@review_tiramisu_router.post(
    '/',
    responses={401: {'description': 'User not found'}},
    dependencies=[Depends(check_user_token)],
)
async def create_review(user_id):
    return user_id
