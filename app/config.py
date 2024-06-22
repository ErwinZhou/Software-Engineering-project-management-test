#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# TODO: Use hierarchical toml file to store configs
from datetime import timedelta
import os

DATABASE_URL = os.environ.get('MYSQL_DATABASE_URL')
# Security Settings
SECRETE_KEY = os.environ.get('JWT_SECRETE_KEY')
JWT_ENCODE_ALGORITHM = 'HS256'
TOKEN_EXPIRE_MINUTES = timedelta(minutes=1800)


