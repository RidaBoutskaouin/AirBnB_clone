#!/usr/bin/python3
"""Defines the Review class inheriting from BaseModel Classe"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review.
    Attributes: place_id (str): The id of the place.
                user_id (str): The id of the user.
                text (str): text.
    """
    place_id = ""
    user_id = ""
    text = ""
