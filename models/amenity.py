#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """
    
    def __init__(self, *args, **kwargs):
        """Initialize the Amenity instance."""
        super().__init__(*args, **kwargs)

        # 'name' is an attribute to store the name of the Amenity.
        self.name = ""
