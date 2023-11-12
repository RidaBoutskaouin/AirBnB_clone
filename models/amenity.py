#!/usr/bin/python3
"""Defines the Amenity class inheriting from BaseModel Classe"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent a Amenity.
    Attributes: name (str): The name of the Amenity.
    """

    name = ""
