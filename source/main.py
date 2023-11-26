from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from source.router import user, review_tiramisu

tiramisu = FastAPI()

tiramisu.include_router(user.router)
tiramisu.include_router(review_tiramisu.router)


@tiramisu.get('/stillalive')
async def still_alive():
    return HTMLResponse('the tiramisu is wet', 200)
