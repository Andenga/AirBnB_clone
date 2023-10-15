#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel  # Import the BaseModel class

# Define the Place class, which inherits from BaseModel
class Place(BaseModel):
    """Represents a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""  # Initialize the 'city_id' attribute to an empty string
    user_id = ""  # Initialize the 'user_id' attribute to an empty string
    name = ""  # Initialize the 'name' attribute to an empty string
    description = ""  # Initialize the 'description' attribute to an empty string
    number_rooms = 0  # Initialize the 'number_rooms' attribute to 0
    number_bathrooms = 0  # Initialize the 'number_bathrooms' attribute to 0
    max_guest = 0  # Initialize the 'max_guest' attribute to 0
    price_by_night = 0  # Initialize the 'price_by_night' attribute to 0
    latitude = 0.0  # Initialize the 'latitude' attribute to 0.0
    longitude = 0.0  # Initialize the 'longitude' attribute to 0.0
    amenity_ids = []  # Initialize the 'amenity_ids' attribute as an empty list

