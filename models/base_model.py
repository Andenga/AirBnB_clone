import uuid
from datetime import datetime

class BaseModel:
    """
    Base class for all models in the AirBnB clone project.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        """
        if kwargs:
            # Reconstruct an object from a dictionary representation
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
            # Remove the __class__ attribute if it exists
            kwargs.pop('__class', None)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of the object.
        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of __dict__ of the instance.
        - A key __class__ is added to the dictionary with the class name of the object.
        - created_at and updated_at are converted to ISO format strings.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict



from models import storage

class BaseModel:
    """
    Base class for all models in the AirBnB clone project.
    """
    def save(self):
        """
        Update the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    # Rest of the BaseModel code remains the same as in your previous messages.