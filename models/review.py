#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """
    
    def __init__(self, *args, **kwargs):
        """Initialize a new Review instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)

        # 'place_id' is an attribute to store the Place ID associated with the review.
        self.place_id = ""

        # 'user_id' is an attribute to store the User ID associated with the review.
        self.user_id = ""

        # 'text' is an attribute to store the text of the review.
        self.text = ""
