from datetime import datetime

import pytz
from beanie import Document
from pydantic import BaseModel

shanghai_tz = pytz.timezone('Asia/Shanghai')


class CreateUser(BaseModel):
    username: str
    password: str
    enable: bool = True
    role: str = 'admin'


class RespUser(BaseModel):
    id: str
    username: str
    hash_password: str
    enable: bool
    role: str
    time: str


class User(Document):
    id: str
    username: str
    hash_password: str
    enable: bool
    role: str
    time: datetime = datetime.now(tz=shanghai_tz)

    class Settings:
        name = 'user'

        class Config:  # 这个子类，表示一个例子
            schema_extra = {
                "example": {
                    'id': '6411233065413',
                    'username': 'ano',
                    'hash_password': 'as5463a2dbf113nja',
                    'enable': True,
                    'role': 'admin',
                    "date": datetime.now()
                }
            }
