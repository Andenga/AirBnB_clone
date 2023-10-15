#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel  # Import the BaseModel class

# Define the User class, which inherits from BaseModel
class User(BaseModel):
    """Represents a User.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""       # Initialize the 'email' attribute as an empty string
    password = ""    # Initialize the 'password' attribute as an empty string
    first_name = ""  # Initialize the 'first_name' attribute as an empty string
    last_name = ""   # Initialize the 'last_name' attribute as an empty string

