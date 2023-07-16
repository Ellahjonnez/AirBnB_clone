#!/usr/bin/python3
"""This function defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
