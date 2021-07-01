#!/usr/bin/python3
"""
Place Module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Instance of BaseModel class
    
    Attributes:
    -----------
    city_id : str
        City.id from City class
    user_id : str
        User.id from User class
    name : str
        Name of the place
    description : str
        Description of the place
    number_rooms : int
        number of rooms
    number_bathrooms : int
        number of bathrooms
    max_guest : int
        maximum guests
    price_by_night : int
        price by night
    latitude : float
        latitude of the place
    longitude : float
        longitude of the place
    amenity_ids : list
        Amenity.id from Amenity class
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    if str:
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
