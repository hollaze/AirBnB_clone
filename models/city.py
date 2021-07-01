#!/usr/bin/python3
"""
City Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Instance of BaseModel class
    
    Attributes:
    -----------
    state_id : str
        State.id from State class
    name : str
        Name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
