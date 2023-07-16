#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.
    """

    city_id = ""   # The City id.
    user_id = ""   # The User id.
    name = ""   # The name of the place.
    description = ""   # The description of the place.
    number_rooms = 0   # The number of rooms of the place.
    number_bathrooms = 0   # The number of bathrooms of the place.
    max_guest = 0   # The maximum number of guests of the place.
    price_by_night = 0   # The price by night of the place.
    latitude = 0.0   # The latitude of the place.
    longitude = 0.0   # The longitude of the place.
    amenity_ids = []   # A list of Amenity ids.
