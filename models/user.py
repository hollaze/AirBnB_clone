#!/usr/bin/python3
"""
User Module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Instance of BaseModel class
    
    Attributes:
    -----------
    email : str
        email of the user
    password : str
        password of the user
    first_name : str
        first name of the user
    last_name : str
        last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
