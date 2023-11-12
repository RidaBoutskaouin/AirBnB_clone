#!/usr/bin/python3

"""Unittest for FileStorage class"""

import unittest
import json
import os

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):

    """Test cases for all methods of FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.file_path = storage._FileStorage__file_path
        self.instance = BaseModel()
        self._objs = storage._FileStorage__objects
        self.keyname = "BaseModel." + self.instance.id

    def tearDown(self):
        """Tear down test environment"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass
        storage._FileStorage__objects = {}

    def test_all(self):
        """Test the all() method"""
        result = storage.all()
        self.assertEqual(result, self._objs)

    def test_new(self):
        """Test the new() method"""
        storage.new(self.instance)
        key = "{}.{}".format(self.instance.__class__.__name__, self.instance.id)
        self.assertIn(key, self._objs)

    def test_save(self):
        """Test the save() method"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        storage.save()

        with open(self.file_path, "r") as f:
            saved_data = json.load(f)

        expected_data = {}
        for key, value in self._objs.items():
            expected_data[key] = value.to_dict()

        self.assertEqual(saved_data, expected_data)

    def test_reload(self):
        """Test the reload() method"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        storage.new(my_model)
        storage.save()

        with open(self.file_path, "r") as f:
            saved_data = json.load(f)

        storage.reload()

        with open(self.file_path, "r") as f:
            reloaded_data = json.load(f)

        self._objs = {}
        self.assertEqual(reloaded_data[self.keyname], saved_data[self.keyname])

    def test_path(self):
        """Test the file path existence"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))
        storage.reload()


if __name__ == "__main__":
    unittest.main()
