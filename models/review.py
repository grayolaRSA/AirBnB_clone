#!/usr/bin/python3
"""module for reviews"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    class for customer reviews based on various attributes
    """

    place_id = ""
    user_id = ""
    text = ""
