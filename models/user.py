#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel

class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    
    def __init__(self, *args, **kwargs):
        """Initialize a new User instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)

        # 'email' is an attribute to store the email of the user.
        self.email = ""

        # 'password' is an attribute to store the password of the user.
        self.password = ""

        # 'first_name' is an attribute to store the first name of the user.
        self.first_name = ""

        # 'last_name' is an attribute to store the last name of the user.
        self.last_name = ""
