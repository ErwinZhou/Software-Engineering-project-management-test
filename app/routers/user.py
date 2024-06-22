#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


from services import user as user_service
from slowapi import Limiter
from slowapi.util import get_remote_address
from schemas import schemas
from schemas.schemas import UserInDB
from utils.database import get_db


limiter = Limiter(key_func=get_remote_address)

user = APIRouter()
@user.post('/register', response_model=schemas.User)
@limiter.limit("10/10minutes")
async def register(request: Request,
                   user: schemas.UserCreate,
                   db: Session = Depends(get_db)):
    user.username = user.username.lower()
    user = user_service.create_user(db, user)
    return user


@user.post('/login', response_model=schemas.Token)
@limiter.limit("10/minute")
async def login(request: Request,
                form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(get_db)):
    form_data.username = form_data.username.lower()
    token = user_service.login(db, form_data.username, form_data.password)
    if token is None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return schemas.Token(access_token=token, token_type="bearer")