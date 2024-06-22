#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import secrets
from typing import Union, Type, Optional

from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

import config
from crud import user as crud
from models.models import User
from schemas.schemas import UserInDB, UserCreate
from utils import security, database


def login(db: Session, username: str, plain_password: str) -> Union[str, None]:
    """
    Generate access token.
    :param db: SQLAlchemy.Session
    :param username
    :param plain_password:
    :return:
    """
    user: User = crud.get_user(db, username)
    if user:
        if not user.is_active:
            raise HTTPException(status_code=400, detail="Inactivated user")
        if security.verify_password(plain_password, user.encoded_password):
            return security.generate_access_jwt(username, config.TOKEN_EXPIRE_MINUTES)
    return None


async def get_current_user_or_none(db: Session = Depends(database.get_db),
                                   token: str = Depends(security.optional_oauth2_scheme)) -> Optional[UserInDB]:
    username = security.extract_username(token)
    if username is None:
        return None
    user = await crud.get_user(db, username)
    return user if user and user.is_active else None


async def get_current_user(db: Session = Depends(database.get_db),
                           token: str = Depends(security.oauth2_scheme)) -> UserInDB:
    """
    For view functions to get current authorized user.
    :param db: SQLAlchemy.Session
    :param token: FastAPI Depends
    :return:
    """
    username = security.extract_username(token)
    return await crud.get_active_user(db, username)


def create_user(db: Session, user: UserCreate) -> User:
    user: User | None = crud.create_user(db, user)
    if user is None:
        raise HTTPException(status_code=400, detail="Username has already existed")
    return user


def refresh_upload_token(db: Session, username: str) -> str:
    user: Type[User] = db.query(User).filter(User.username == username).one()
    user.upload_token = secrets.token_hex(32)
    db.commit()
    db.refresh(user)

    return user.upload_token
