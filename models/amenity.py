#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel

# Define the Amenity class, which inherits from BaseModel
class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

