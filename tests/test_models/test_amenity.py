#!/usr/bin/python3
"""Unittest for Amenity class"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""
    def setUp(self):
        """Set up for all tests"""
        self.amenity = Amenity()

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_str(self):
        """Test __str__"""
        string = str(self.amenity)
        self.assertIn("[Amenity]", string)
        self.assertIn("'id':", string)
        self.assertIn("'created_at':", string)
        self.assertIn("'updated_at':", string)

    def test_to_dict(self):
        """Test to_dict"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)

    def test_from_dict(self):
        """Test from_dict"""
        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity()
        new_amenity.from_dict(amenity_dict)
        self.assertEqual(self.amenity.id, new_amenity.id)
        self.assertEqual(self.amenity.created_at, new_amenity.created_at)
        self.assertEqual(self.amenity.updated_at, new_amenity.updated_at)
        self.assertEqual(self.amenity.name, new_amenity.name)

    def test_save(self):
        """Test save"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_kwargs(self):
        """Test kwargs"""
        amenity_dict = {"id": "123", "name": "Wifi"}
        new_amenity = Amenity(**amenity_dict)
        self.assertEqual(new_amenity.id, "123")
        self.assertEqual(new_amenity.name, "Wifi")

if __name__ == "__main__":
    unittest.main()
