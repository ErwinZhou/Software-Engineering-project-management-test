#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    userName: str = Field(..., min_length=2, max_length=255)
    user_id: int
    password: str = Field(..., min_length=5)
    name: str
    gender: str
    age: int
    phone_number: str
    email: EmailStr
    role: str


class User(UserBase):
    class Config:
        from_attributes = True


class UserInDB(UserBase):
    encoded_password: str

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    username: str = Field(pattern=r'^[A-Za-z][A-Za-z0-9_]{5,15}$')
    email: EmailStr
    # TODO: 适配 Pydantic 的 Rust-style regex 校验
    password: str


class LoginInfo(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UploadToken(BaseModel):
    upload_token: str
