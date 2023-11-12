#!/usr/bin/python3
""" Base Model Module """

import uuid
from datetime import datetime
import models


class BaseModel:
    """A class BaseModel that defines all common attributes/methods
    for other classes."""

    def __init__(self, *args, **kwargs):
        """initializes the public instance attributes"""
        time_str = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, time_str))
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """__str__ method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of instance"""
        diction = dict(self.__dict__)
        diction["__class__"] = self.__class__.__name__
        diction["created_at"] = \
            self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        diction["updated_at"] = \
            self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return diction
