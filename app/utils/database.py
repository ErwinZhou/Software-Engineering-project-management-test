#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json

from sqlalchemy.orm import Session
from sqlalchemy.exc import AmbiguousForeignKeysError

from models import database, models
from models.database import SessionLocal

def init_db():
    database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
