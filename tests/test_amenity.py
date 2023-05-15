#!/usr/bin/python3
"""module to test amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """class to test amenity class"""
    def test_attributes(self):
        """Test that the Amenity class has the correct attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        """Test that the Amenity class inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
