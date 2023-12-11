from typing import Callable

from motor.motor_asyncio import AsyncIOMotorClient
import uvicorn
from fastapi import FastAPI, APIRouter
from beanie import init_beanie

from model.user import User
from api import user_router

application = FastAPI()

url = "mongodb://192.168.17.131:27017"


def startup() -> Callable:
    async def init_mongo():
        client = AsyncIOMotorClient(url)
        await init_beanie(database=client.beanie, document_models=[User])

    return init_mongo


application.add_event_handler('startup', startup())

application.include_router(user_router)
app = application


@application.get("/info")
async def user_info() -> dict:
    return {
        'nickname': 'ano',
        'email': "3355698298@qq.com"
    }


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
