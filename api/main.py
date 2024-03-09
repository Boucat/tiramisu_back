from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from api.router.review_tiramisu import review_tiramisu_router
from api.router.tiramisu import tiramisu_router
from api.router.user import user_router

# Create an instance of FastAPI
tiramisu = FastAPI(
    title='Tiramisu.cat API',
    description='Today is a fantastic day to APIfy a Tiramisu',
    version='1.0.0',
    openapi_url='/docs/openapi.json',
    docs_url='/docs/documentation',
    redoc_url='/docs/redoc',
)


@tiramisu.get('/stillalive', include_in_schema=False)
async def still_alive():
    return HTMLResponse('the tiramisu is wet', 200)


tiramisu.include_router(authorization_router, prefix='/v1')

# tiramisu.include_router(user_router, prefix='/v1')

# tiramisu.include_router(tiramisu_router, prefix='/v1')

# tiramisu.include_router(review_tiramisu_router, prefix='/v1')
