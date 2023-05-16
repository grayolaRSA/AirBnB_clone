#!/usr/bin/python3
"""module to test review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """class for test review class"""
    def setUp(self):
        """Set up for testing"""
        self.review = Review()

    def test_attributes(self):
        """Test that the Review class has the correct attributes"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_inheritence(self):
        """Test that Review class inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))
