#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file (JSON serialization)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Loads storage dictionary from file (JSON deserialization)"""
        if os.path.exists(self.__file_path) is True:
            try:
                with open(self.__file_path, mode="r", encoding="utf-8") as f:
                    new_dict = json.load(f)
                for key, value in new_dict.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
            except FileNotFoundError:
                pass
