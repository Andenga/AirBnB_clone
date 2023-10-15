#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel

# Define the Review class, which inherits from BaseModel
class Review(BaseModel):
    """Represents a review.

    Attributes:
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The written content of the review.
    """

    place_id = ""  # Initialize place_id attribute as an empty string
    user_id = ""   # Initialize user_id attribute as an empty string
    text = ""      # Initialize text attribute as an empty string

