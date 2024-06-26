#!/usr/bin/python3

import json as js
from os import path
from models.base_model import BaseModel

"""This file contains the class file storage for storing dict  in json file"""


class FileStorage:
    """This class has few functions or method to work with"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            tok = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[tok] = obj

    def save(self):
        if self.__objects:
            new_obj = {}
            for k in self.__objects.keys():
                new_obj[k] = self.__objects[k].to_dict()
            with open(self.__file_path, "w", encoding="utf-8") as f:
                js.dump(new_obj, f)

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                __obj = js.load(f)
                for v in __obj.values():
                    __new = "{}(**v)".format(v["__class__"])
                    __ob = eval(__new)
                    self.new(__ob)
        else:
            pass
