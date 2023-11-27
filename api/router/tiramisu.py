from fastapi import APIRouter, HTTPException

from api import USERS

tiramisu_router = APIRouter(
    prefix='/tiramisu',
    tags=['tiramisu'],
    responses={404: {'description': 'Not found'}},
)


# Endpoint to get all tiramisus from a user
@tiramisu_router.get('/{user_id}')
async def get_tiramisus_from_user(user_id: str):
    get_all_users = [user.get('id') for user in USERS]
    if user_id in get_all_users:
        return {'all your tiramisus': 'are the best Sr. ' + user_id}
    else:
        return HTTPException(status_code=404, detail=f'User {user_id} not found')
