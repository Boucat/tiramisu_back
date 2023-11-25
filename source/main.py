from fastapi import FastAPI
from fastapi.responses import HTMLResponse

tiramisu = FastAPI()


@tiramisu.get('/stillalive')
async def still_alive(status_code=200):
    return HTMLResponse('the tiramisu is wet', 200)
