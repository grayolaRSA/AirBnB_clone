#!/usr/bin/python3
"""module to test city class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """class to test city class"""
    def test_attributes(self):
        """Test that the City class has the correct attributes"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_inheritance(self):
        """Test that the City class inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
