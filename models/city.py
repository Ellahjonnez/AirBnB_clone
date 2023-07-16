#!/usr/bin/python3
"""This model defines the class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent the city class.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
