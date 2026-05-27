#!/usr/bin/python3
"""This module defines the Review class"""
from models.tmp_base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
