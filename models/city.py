#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel  # Import the BaseModel class

# Define the City class, which inherits from BaseModel
class City(BaseModel):
    """Represents a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""  # Initialize the 'state_id' attribute to an empty string
    name = ""  # Initialize the 'name' attribute to an empty string

