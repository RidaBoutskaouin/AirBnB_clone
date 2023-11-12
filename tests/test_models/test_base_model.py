#!/usr/bin/python3

"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import json
import os


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base = BaseModel()

    def tearDown(self):
        del self.base

    def test_id(self):
        """Test id is string"""
        self.assertIsInstance(self.base.id, str)

    def test_unique_id(self):
        """Test id is unique"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_created_at(self):
        """Test created_at is datetime"""
        self.assertIsInstance(self.base.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at is datetime"""
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test updated_at changes on save"""
        old_update = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_update, self.base.updated_at)

    def test_to_dict_type(self):
        """Test to_dict returns dict"""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)

    def test_to_dict_keys(self):
        """Test to_dict has correct keys"""
        base_dict = self.base.to_dict()
        self.assertIn("id", base_dict)
        self.assertIn("created_at", base_dict)
        self.assertIn("updated_at", base_dict)
        self.assertIn("__class__", base_dict)

    def test_str_format(self):
        """Test str format"""
        self.assertEqual(
            str(self.base),
            "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__),
        )

    def test_kwargs_instantiation(self):
        """Test instantiation from kwargs"""
        base_dict = self.base.to_dict()
        new_base = BaseModel(**base_dict)
        self.assertEqual(new_base.id, self.base.id)
        self.assertEqual(new_base.created_at, self.base.created_at)
        self.assertEqual(new_base.updated_at, self.base.updated_at)

    def test_kwargs_new_instantiation(self):
        """Test instantiation from kwargs reuses id"""
        
        base = BaseModel()
        base_dict = base.to_dict()
        
        # Create new instance from kwargs
        new_base = BaseModel(**base_dict)
        
        # Check if id is reused
        self.assertEqual(new_base.id, base.id)  
        
        # Check for equality of other attributes
        self.assertEqual(new_base.created_at, base.created_at)
        self.assertEqual(new_base.updated_at, base.updated_at)


if __name__ == "__main__":
    unittest.main()
