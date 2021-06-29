#!/usr/bin/python3
"""
BaseModel Module
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    defines all common attributes/methods for other classes

    Attributes:
    -----------
    args : Any
        Arguments
    kwargs : dict[str, Any]
        key, value for __dict__

    Methods:
    --------
    save():
        Update updated_at with the current datetime
        and saves it into a file.json
    to_dict():
        Changes format of datetime to isoformat
        Returns a new dictionnary containing all key/values
        of __dict__
    """

    def __init__(self, *args, **kwargs):
        """
        Constructs Attributes for the __dict__ of the class

        Parameters:
        -----------
            args: Any
                arguments
            kwargs : dict[str, Any]
                key, value for __dict__
        """
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
        """
        Prints: <classname> <classname.id> <__dict__>
        """
        return "[{}] ({:s}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
        """
        Update updated_at with the current datetime
        and saves it into a file.json
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Changes format of datetime to isoformat
        Returns a new dictionnary containing all key/values
        of __dict__
        """
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
