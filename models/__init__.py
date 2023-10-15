#!/usr/bin/python3
"""__init__ magic method for models directory"""

# Import the FileStorage class from the "models.engine.file_storage" module.
from models.engine.file_storage import FileStorage

# Create an instance of the FileStorage class, which manages file-based storage.
storage = FileStorage()

# Reload the data from storage (if any) into the storage instance.
storage.reload()
#!/usr/bin/python3
