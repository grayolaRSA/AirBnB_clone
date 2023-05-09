#!/usr/bin/python3
"""module for reviews"""


class Review(BaseModel):
    """
    class for customer reviews based on various attributes
    """

    place_id = ""
    user_id = ""
    text = ""
