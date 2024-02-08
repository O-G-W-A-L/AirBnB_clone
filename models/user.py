#!/usr/bin/python3
"""module creates the user class"""

from models.base_model import BaseModel

class User(BaseModel):
    """class user for managing user objects"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
