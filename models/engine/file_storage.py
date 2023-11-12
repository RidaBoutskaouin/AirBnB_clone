#!/usr/bin/python3

"""
FileStorage Module

This module manages the serialization and deserialization
of objects to and from JSON files.

Classes:
- FileStorage: Manages the storage and
retrieval of instances to/from JSON files.

Attributes:
- __file_path (str): The path to the JSON file.
- __objects (dict): A dictionary to store instances by their class name and ID.

Methods:
- all(self): Returns the dictionary of stored objects.
- new(self, obj): Adds an object to the storage.
- save(self): Serializes the objects and saves to the JSON file.
- reload(self): Deserializes the JSON file and loads objects.

Usage:
from models.engine.file_storage import FileStorage

# Instantiate FileStorage
storage = FileStorage()

# Load existing object data from the JSON file
storage.reload()

# Perform operations on instances (create, update, delete)
# Call storage.save() after each operation to persist changes

"""

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
