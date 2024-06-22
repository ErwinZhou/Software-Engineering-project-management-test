#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

current_user_id = 0


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)  # 用户编号
    username = Column(String(255))  # 用户名
    password = Column(String(255))  # 密码
    name = Column(String(255))  # 姓名
    gender = Column(String(255))  # 性别
    age = Column(Integer)  # 年龄
    phone_number = Column(String(255))  # 电话号码
    email = Column(String(255))  # 邮箱地址
    role = Column(String(255))  # 职位