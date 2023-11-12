#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def setUp(self):
        """Set up test methods"""
        self.amenity = Amenity()
        self.amenity.name = "Wifi"

    def tearDown(self):
        """Tear down test methods"""
        pass

    def test_instance(self):
        """Test for correct instancing of Amenity object"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_inheritance(self):
        """Test for correct inheritance of Amenity object"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attributes(self):
        """Test for correct attributes"""
        self.assertTrue("name" in self.amenity.__dict__)

    def test_save(self):
        """Test for correct save functionality"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_str(self):
        """Test for correct str output"""
        self.assertEqual(
            str(self.amenity),
            "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__),
        )

    def test_to_dict(self):
        """Test for correct dictionary output"""
        self.assertEqual("to_dict" in dir(self.amenity), True)
    

if __name__ == "__main__":
    unittest.main()

