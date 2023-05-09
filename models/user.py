#!/usr/bin/python3
"""module for user class"""


class User(BaseModel):
    """
    User class that inherits from base model
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
