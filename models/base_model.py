#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    new_value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, new_value)
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        return "[{}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if not value:
                continue
            if key == "created_at" or key == "updated_at":
                new_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                new_dict[key] = value
        return new_dict
