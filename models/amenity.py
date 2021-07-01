#!/usr/bin/python3
"""
Amenity Module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Instance of BaseModel class
    
    Attribute:
    ----------
    name : str
        Name of the amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
