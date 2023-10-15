#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage  # Import the FileStorage class

# Create an instance of the FileStorage class
storage = FileStorage()

# Reload (deserialize) the data from the JSON file into the storage
storage.reload()

