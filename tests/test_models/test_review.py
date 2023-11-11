#!/usr/bin/python3
"""Unittest for Review class"""

import unittest
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def setUp(self):
        """Set up for all tests"""
        self.review = Review()
        self.review.place_id = "San Francisco"
        self.review.user_id = "CA"
        self.review.text = "San Francisco"

    def tearDown(self):
        """Tear down for all tests"""
        del self.review

    def test_docstring(self):
        """Test docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue("id" in self.review.__dict__)
        self.assertTrue("created_at" in self.review.__dict__)
        self.assertTrue("updated_at" in self.review.__dict__)
        self.assertTrue("place_id" in self.review.__dict__)
        self.assertTrue("user_id" in self.review.__dict__)
        self.assertTrue("text" in self.review.__dict__)

    def test_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_type(self):
        """Test type of Review"""
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)
