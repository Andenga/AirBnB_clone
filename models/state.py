#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel

# Define the State class, which inherits from BaseModel
class State(BaseModel):
    """Represents a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""  # Initialize the name attribute as an empty string

