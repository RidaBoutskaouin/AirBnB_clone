#!/usr/bin/python3
"""Defines the City class inheriting from BaseModel Classe"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a City.
    Attributes: state_id (str): The state id.
    name (str): name of the city.
    """
    state_id = ""
    name = ""
