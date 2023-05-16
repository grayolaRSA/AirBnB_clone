#!/usr/bin/python3
"""module for unittests for state class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """class to test state class"""
    def test_attributes(self):
        """Test that the State class has the correct attributes"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        """Test that the State class inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
