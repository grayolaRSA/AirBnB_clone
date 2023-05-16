#!/usr/bin/python3
"""module for amenities"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class for amenities
    """

    def __init__(self, *args, **kwargs):
        """Creates new instances of Amenity.
        """
        super().__init__(*args, **kwargs)
