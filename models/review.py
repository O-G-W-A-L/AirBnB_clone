#!/usr/bin/env python3
"""Review class module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel class"""

    place_id = ''
    user_id = ''
    text = ''
