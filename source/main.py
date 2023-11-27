from fastapi import APIRouter, FastAPI
from fastapi.responses import HTMLResponse

# Create an instance of APIRouter
router = APIRouter()

# Create an instance of FastAPI
tiramisu = FastAPI(
    title="Tiramisu.cat API",
    description="Today is a fantastic day to APIfy a Tiramisu",
    version="1.0.0",
    openapi_url="/docs/openapi.json",
    docs_url="/docs/documentation",
    redoc_url="/docs/redoc",
)

# Include the router in the main app
tiramisu.include_router(router, prefix="/source")


@tiramisu.get('/stillalive', include_in_schema=False)
async def still_alive():
    return HTMLResponse('the tiramisu is wet', 200)
