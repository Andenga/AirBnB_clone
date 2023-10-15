#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel

# Define the Amenity class, which inherits from the BaseModel class
class Amenity(BaseModel):
    """Represents an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""  # Initialize the 'name' attribute to an empty string

