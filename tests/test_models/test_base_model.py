#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
import json
import os


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test methods"""
        self.base = BaseModel()

    def tearDown(self):
        """Tear down test methods"""
        pass

    def test_instance(self):
        """Test for correct instancing of BaseModel object"""
        self.assertIsInstance(self.base, BaseModel)

    def test_inheritance(self):
        """Test for correct inheritance of BaseModel object"""
        self.assertTrue(issubclass(self.base.__class__, BaseModel), True)

    def test_attributes(self):
        """Test for correct attributes"""
        self.assertTrue("id" in self.base.__dict__)
        self.assertTrue("created_at" in self.base.__dict__)
        self.assertTrue("updated_at" in self.base.__dict__)

    def test_save(self):
        """Test for correct save functionality"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_str(self):
        """Test for correct str output"""
        self.assertEqual(
            str(self.base),
            "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__),
        )

    def test_to_dict(self):
        """Test for correct dictionary output"""
        self.assertEqual("to_dict" in dir(self.base), True)

    def test_kwargs(self):
        """Test for correct instantiation from kwargs"""
        self.base.name = "Holberton"
        self.base.my_number = 89
        self.base.save()
        self.base_json = self.base.to_dict()
        self.base_new = BaseModel(**self.base_json)
        self.assertEqual(self.base_new.id, self.base.id)
        self.assertEqual(self.base_new.created_at, self.base.created_at)
        self.assertEqual(self.base_new.updated_at, self.base.updated_at)
        self.assertEqual(self.base_new.name, self.base.name)
        self.assertEqual(self.base_new.my_number, self.base.my_number)


if __name__ == "__main__":
    unittest.main()
