#!/usr/bin/python3

import json


class FileStorage:
    __file_path = "file_storage.json"
    __objects = {}

    def all(self):
        for key, value in self.__objects:
            return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        save_obj = {}
        for key in self.__objects:
            save_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'a', encoding='utf-8') as file:
            json.dump(save_obj, file)

    def reload(self):
        try:
            if self.__file_path:
                with open(self.__file_path, 'r', encoding='utf-8') as file:
                    json.load(file)
        except:
            pass
