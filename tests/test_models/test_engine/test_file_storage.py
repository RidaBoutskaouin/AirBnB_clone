#!/usr/bin/python3
"""unittests for FileStorage class"""

import unittest
import pep8
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up class before start testing"""
        cls.fs = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Remove storage file at end of tests"""
        del cls.fs
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """Test pep8 styling"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 0)

    def test_docstring(self):
        """Test docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_class_docstring(self):
        """Test class docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_fs_is_instance(self):
        """Test if fs is an instance of FileStorage"""
        self.assertIsInstance(self.fs, FileStorage)

    def test_all(self):
        """Test all method"""
        self.assertIsInstance(self.fs.all(), dict)

    def test_new(self):
        """Test new method"""
        bm = BaseModel()
        self.fs.new(bm)
        self.assertIn("BaseModel." + bm.id, self.fs.all().keys())

    def test_save(self):
        """Test save method"""
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + bm.id, f.read())

    def test_reload(self):
        """Test reload method"""
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        storage.reload()
        self.assertIn("BaseModel." + bm.id, storage.all().keys())
