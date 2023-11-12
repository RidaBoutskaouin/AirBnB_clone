#!/usr/bin/python3

"""Unittest for City class"""

import unittest
from models.city import City
from datetime import datetime
from models.base_model import BaseModel

class TestCityInstance(unittest.TestCase):
    
    """Test City class instance"""
    
    def setUp(self):
        print("Testing City instance...")
        
    def test_city_subclass(self):
        """Test City is subclass of BaseModel"""
        city = City()
        self.assertTrue(isinstance(city, BaseModel))

    def test_different_ids(self):
        """Test City instances have different ids"""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)
        
    def test_id_type(self):
        """Test id is string"""
        city = City()
        self.assertEqual(type(city.id), str)
        
    def test_created_updated_diff(self):
        """Test created and updated diff"""
        city = City()
        self.assertNotEqual(city.created_at, city.updated_at)
        
    def test_attrs_init_empty(self):
        """Test attrs init as empty"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

class TestCityAttrs(unittest.TestCase):

    """Test attributes inherited from BaseModel"""
    
    def setUp(self):
        print("Testing City attributes...")
        
    def test_has_id(self):
        """Test City has id attr"""
        city = City()
        self.assertTrue(city.id)
        
    def test_has_created_at(self):
        """Test City has created_at attr"""
        city = City()
        self.assertTrue(city.created_at)
        
    def test_has_updated_at(self):
        """Test City has updated_at attr"""
        city = City()
        self.assertTrue(city.updated_at)
        
    def test_has_str(self):
        """Test City has __str__ attr"""
        city = City()
        self.assertTrue(city.__str__)
        
    def test_has_dict(self):
        """Test City has to_dict attr"""
        city = City()
        self.assertTrue(city.to_dict)
        
class TestCityKVArgs(unittest.TestCase):

    """Test City kwags in init"""
    
    def test_kwargs(self):
        """Test passing kwargs in init"""
        city = City(name="San Francisco")
        self.assertEqual(city.name, "San Francisco")
        
if __name__ == "__main__":
    unittest.main()
