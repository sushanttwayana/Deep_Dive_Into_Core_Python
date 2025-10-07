from fastapi import APIRouter, status, Request, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from ..database.core import DbSession
from ..rate_limiting import limiter
from . import models
from . import service

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
@limiter.limit("5/hour")
async def register_user(
    request: Request,
    db: DbSession, # type: ignore
    register_user_request: models.RegisterUserRequest
):
    service.register_user(db, register_user_request)
    return {"message": "User registered successfully"}


@router.post("/token", response_model=models.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: DbSession # type: ignore
):
    return service.login_for_access_token(form_data, db)