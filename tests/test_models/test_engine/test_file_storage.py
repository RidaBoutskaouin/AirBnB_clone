#!/usr/bin/python3
"""Unittest for file_storage.py"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Tear down test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        self.storage._FileStorage__objects = {}

    def test_all(self):
        """Test the all method"""
        # Ensure all returns an empty dict when there are no objects
        self.assertEqual(self.storage.all(), {})

        # Ensure all returns a dict of all objects when there are objects
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.assertEqual(self.storage.all(),
                         {"BaseModel.{}".format(obj1.id): obj1,
                         "BaseModel.{}".format(obj2.id): obj2})

    def test_new(self):
        """Test the new method"""
        # Ensure new adds an object to the objects dict
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(self.storage.all(),
                         {"BaseModel.{}".format(obj.id): obj})

    def test_save(self):
        """Test the save method"""
        # Ensure save writes to file.json
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel.{}".format(obj.id), f.read())

    def test_reload(self):
        """Test the reload method"""
        self.storage.new(BaseModel())
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        for obj in self.storage.all().values():
            self.assertIsInstance(obj, BaseModel)
        self.assertEqual(len(self.storage.all()), 1)


if __name__ == "__main__":
    unittest.main()
