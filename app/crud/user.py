#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from typing import Optional

from sqlalchemy.orm import Session

from schemas import schemas
from models.models import User
from models.models import current_user_id
from utils import security


def get_user(db: Session, username: str) -> Optional[User]:
    db_user = db.query(User).filter(User.username == username).first()
    return db_user


def create_user(db: Session, user: schemas.UserCreate) -> Optional[User]:
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        return None

    db_user = User(
        user_id=current_user_id + 1,
        username=user.username,
        password=security.encode_password(user.password),
        name=None,
        gender=None,
        age=None,
        phone_number = None,
        email = user.email,
        role = user.role
    )
    current_user_id += 1
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
