#!/usr/bin/python3
"""Unittest for Place class"""

import unittest
from models.place import Place
from datetime import datetime
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def setUp(self):
        """Set up for all tests"""
        self.place = Place()
        self.place.city_id = "San Francisco"
        self.place.user_id = "CA"
        self.place.name = "San Francisco"
        self.place.description = "San Francisco"
        self.place.number_rooms = 1
        self.place.number_bathrooms = 1
        self.place.max_guest = 1
        self.place.price_by_night = 1
        self.place.latitude = 1.0
        self.place.longitude = 1.0
        self.place.amenity_ids = ["wifi", "cable_tv"]

    def tearDown(self):
        """Tear down for all tests"""
        del self.place

    def test_docstring(self):
        """Test docstring"""
        self.assertIsNotNone(Place.__doc__)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue("id" in self.place.__dict__)
        self.assertTrue("created_at" in self.place.__dict__)
        self.assertTrue("updated_at" in self.place.__dict__)
        self.assertTrue("city_id" in self.place.__dict__)
        self.assertTrue("user_id" in self.place.__dict__)
        self.assertTrue("name" in self.place.__dict__)
        self.assertTrue("description" in self.place.__dict__)
        self.assertTrue("number_rooms" in self.place.__dict__)
        self.assertTrue("number_bathrooms" in self.place.__dict__)
        self.assertTrue("max_guest" in self.place.__dict__)
        self.assertTrue("price_by_night" in self.place.__dict__)
        self.assertTrue("latitude" in self.place.__dict__)
        self.assertTrue("longitude" in self.place.__dict__)
        self.assertTrue("amenity_ids" in self.place.__dict__)

    def test_subclass(self):
        """Test if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_type(self):
        """Test type of Place"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
