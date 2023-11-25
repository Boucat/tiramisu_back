from fastapi import FastAPI

tiramisu = FastAPI()


@tiramisu.get("/")
async def root():
    return {"message": "Hello World"}