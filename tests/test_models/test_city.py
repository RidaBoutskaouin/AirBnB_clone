#!/usr/bin/python3
"""Unittest for City class"""
import unittest
from models.city import City
from datetime import datetime
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def setUp(self):
        """Set up for all tests"""
        self.city = City()
        self.city.name = "San Francisco"
        self.city.state_id = "CA"

    def tearDown(self):
        """Tear down for all tests"""
        del self.city

    def test_docstring(self):
        """Test docstring"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue("id" in self.city.__dict__)
        self.assertTrue("created_at" in self.city.__dict__)
        self.assertTrue("updated_at" in self.city.__dict__)
        self.assertTrue("name" in self.city.__dict__)
        self.assertTrue("state_id" in self.city.__dict__)

    def test_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_type(self):
        """Test type of City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save(self):
        """Test save"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual("to_dict" in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
