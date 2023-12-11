import http

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from model.user import User, CreateUser, RespUser

user_router = APIRouter(
    prefix='/user',
    tags=['User-API']
)


@user_router.post('/create')
async def create_user(user: CreateUser):
    create_userdb = User(
        id='#8751297',
        username=user.username,
        hash_password=user.password,
        enable=user.enable,
        role=user.role
    )
    try:
        await create_userdb.create()
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="create in mongo failed !"
        )
    respdata = RespUser(
        id=create_userdb.id,
        username=create_userdb.username,
        hash_password=create_userdb.hash_password,
        enable=create_userdb.enable,
        role=create_userdb.role,
        time=create_userdb.time.isoformat()
    )
    return JSONResponse(status_code=http.HTTPStatus.OK, content=respdata.__dict__)
