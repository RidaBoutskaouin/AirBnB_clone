#!/usr/bin/python3
"""Defines the State class inheriting from BaseModel Classe"""

from models.base_model import BaseModel


class State(BaseModel):
    """Represent a State.
        Attributes: name (str): name Of the state.
    """
    name = ""
