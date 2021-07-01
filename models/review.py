#!/usr/bin/python3
"""
Review Module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Instance of BaseModel class
    
    Attributes:
    -----------
    place_id : str
        Place.id from Place class
    user_id : str
        User.id from User class
    Text : str
        Review from user
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
