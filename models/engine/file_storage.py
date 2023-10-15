#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

# Define the FileStorage class for storing and managing objects
class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"  # Default JSON file path
    __objects = {}  # Dictionary to store objects

    # Method to retrieve all stored objects
    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    # Method to add a new object to the dictionary
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__  # Get the class name
        # Create a key in the format "class_name.id"
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    # Method to serialize objects to a JSON file
    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects  # Get the objects dictionary
        # Create a dictionary of object IDs and their serialized representations
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        # Open the JSON file for writing and save the object data
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    # Method to deserialize objects from the JSON file
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)  # Load data from the JSON file
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]  # Remove the class name from the dictionary
                    # Create a new object of the specified class with the loaded data
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return  # Handle the case where the JSON file does not exist

