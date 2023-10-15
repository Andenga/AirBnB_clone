#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel

class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """
    
    def __init__(self, *args, **kwargs):
        """Initialize a new State instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)

        # 'name' is an attribute to store the name of the state.
        self.name = ""
