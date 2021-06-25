#!/usr/bin/python3
from models.base_model import BaseModel
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        obj_key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[obj_key] = obj

    def save(self):
        save_obj = {}
        for key in self.__objects:
            save_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dumps(save_obj, f)

    def reload(self):
        with open(self.__file_path, 'r') as f:
            reload = json.loads(f) 








