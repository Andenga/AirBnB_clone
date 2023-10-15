#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

# Define the BaseModel class
class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())  # Generate a unique ID using uuid4
        self.created_at = datetime.today()  # Set the creation timestamp
        self.updated_at = datetime.today()  # Set the update timestamp
        if len(kwargs) != 0:  # Check if keyword arguments are provided
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    # If key is created_at or updated_at, parse the datetime
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v  # Set other attributes from kwargs
        else:
            models.storage.new(self)  # If no kwargs, add the instance to storage

    def save(self):
        """Update updated_at with the current datetime and save the object."""
        self.updated_at = datetime.today()  # Update the update timestamp
        models.storage.save()  # Save the object using the storage mechanism

    def to_dict(self):
        """Return the dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()  # Create a copy of the instance's dictionary
        rdict["created_at"] = self.created_at.isoformat()  # Format created_at
        rdict["updated_at"] = self.updated_at.isoformat()  # Format updated_at
        rdict["__class__"] = self.__class__.__name__  # Add class name
        return rdict  # Return the dictionary

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        clname = self.__class__.__name__  # Get the class name
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)  # Format and return the string

