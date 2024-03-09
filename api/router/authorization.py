from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from api import *
from api.service import token_service, user_service

authorization_router = APIRouter(prefix='/authorization')


class Token(BaseModel):
    access_token: str
    token_type: str
    ttl: int


class TokenData(BaseModel):
    username: str | None = None


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@authorization_router.post('/token')
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = user_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token_service.create_access_token(data={'sub': user.username}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type='bearer', ttl=ACCESS_TOKEN_EXPIRE_MINUTES * 60)
