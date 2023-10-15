#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel

class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price per night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """
    
    def __init__(self, *args, **kwargs):
        """Initialize a new Place instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)

        # 'city_id' is an attribute to store the City ID associated with the place.
        self.city_id = ""

        # 'user_id' is an attribute to store the User ID associated with the place.
        self.user_id = ""

        # 'name' is an attribute to store the name of the place.
        self.name = ""

        # 'description' is an attribute to store the description of the place.
        self.description = ""

        # 'number_rooms' is an attribute to store the number of rooms in the place.
        self.number_rooms = 0

        # 'number_bathrooms' is an attribute to store the number of bathrooms in the place.
        self.number_bathrooms = 0

        # 'max_guest' is an attribute to store the maximum number of guests for the place.
        self.max_guest = 0

        # 'price_by_night' is an attribute to store the price per night for the place.
        self.price_by_night = 0

        # 'latitude' is an attribute to store the latitude of the place.
        self.latitude = 0.0

        # 'longitude' is an attribute to store the longitude of the place.
        self.longitude = 0.0

        # 'amenity_ids' is an attribute to store a list of Amenity IDs associated with the place.
        self.amenity_ids = []
#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel

    longitude = 0.0
    amenity_ids = []
