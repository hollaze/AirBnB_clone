#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.base_model import Place
from models.base_model import City
from models.base_model import User
from models.base_model import State
from models.base_model import Review
from models.base_model import Amenity
from models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):

        new_obj = obj.__class__.__name__ + "." + obj.id
        self.__objects[new_obj] = obj

    def save(self):
        file_obj = {}
        for key in self.__objects:
            file_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(file_obj, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                dict_file = {}
                dict_file = json.load(file)
                for key, value in dict_file.items():
                    self.new(eval(value['__class__'])(**value)) 
        except Exception:
            pass
