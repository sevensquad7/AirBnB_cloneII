#!/usr/bin/python3
"""Class User"""
from models.base_model import BaseModel

class User(BaseModel):
    """User data"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
