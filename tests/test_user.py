#!/usr/bin/python3
"""test module for the user base class module"""
import unittest
from models.user import User
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def test_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_storage(self):
        user = User()
        user.email = "test@test.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        storage.new(user)
        key = "User." + user.id
        obj = storage.all().get(key)
        self.assertIsNotNone(obj)
        self.assertIsInstance(obj, User)
        self.assertEqual(obj.email, "test@test.com")
        self.assertEqual(obj.password, "password")
        self.assertEqual(obj.first_name, "John")
        self.assertEqual(obj.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
