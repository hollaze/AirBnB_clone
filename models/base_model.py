#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if kwargs is not None:
            self.__dict__.update(kwargs) 
        
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            

    def __str__(self):
        return "[{}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        key = self.__class__.__name__
        for key in self.__dict__.keys():
            return self.__dict__

