#!/usr/bin/python3
"""Unittest for State class"""

import unittest
from models.state import State
from datetime import datetime
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def setUp(self):
        """Set up for all tests"""
        self.state = State()
        self.state.name = "San Francisco"

    def tearDown(self):
        """Tear down for all tests"""
        del self.state

    def test_docstring(self):
        """Test docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue("id" in self.state.__dict__)
        self.assertTrue("created_at" in self.state.__dict__)
        self.assertTrue("updated_at" in self.state.__dict__)
        self.assertTrue("name" in self.state.__dict__)

    def test_subclass(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_type(self):
        """Test type of State"""
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        """Test save"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """Test to_dict"""
        self.assertEqual("to_dict" in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
