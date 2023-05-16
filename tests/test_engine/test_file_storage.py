#!/usr/bin/python3
"""module for testing the file storage class"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.bm = BaseModel()

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                f.write("{}")

    def test_all(self):
        """Test for all method"""
        self.assertEqual(type(self.storage.all()), dict)
        self.assertIs(self.storage.all(), self.storage._FileStorage__objects)

    def test_new(self):
        """Test for new method"""
        key = self.bm.__class__.__name__ + "." + self.bm.id
        self.storage.new(self.bm)
        self.assertIn(key, self.storage._FileStorage__objects.keys())
        self.assertIn(self.bm, self.storage._FileStorage__objects.values())

    def test_save(self):
        """Test for save method"""
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        with open(self.file_path, "r") as f:
            objs = json.load(f)
        obj_key = "{}.{}".format(type(bm).__name__, bm.id)
        self.assertIn(obj_key, objs.keys())

    def test_reload(self):
        """Test for reload method"""
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        self.storage.reload()
        objs = self.storage.all()
        obj_key = "{}.{}".format(type(bm).__name__, bm.id)
        self.assertIn(obj_key, objs.keys())

    def tearDown(self):
        """Remove file.json created"""
        try:
            os.remove(self.file_path)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    unittest.main()
