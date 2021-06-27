#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    new_value = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, new_value)
                elif key != "__class__":
                    setattr(self, key, value)

        models.storage.new(self)

    def __str__(self):
        return "[{}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

