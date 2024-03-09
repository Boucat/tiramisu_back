from fastapi import APIRouter


tiramisu_router = APIRouter(
    prefix='/tiramisu',
    tags=['tiramisu'],
    responses={404: {'description': 'Not found'}},
)


# Endpoint to get all tiramisus from a user
@tiramisu_router.get('/{user_id}')
async def get_tiramisus_from_user(user_id: str):
    pass
