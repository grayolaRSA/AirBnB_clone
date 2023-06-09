#!/usr/bin/python3
"""module for testing the file storage class"""
import unittest
import json
import os
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    @classmethod
    def setUp(cls):
        """Runs for each test case.
        """
        from models.engine.file_storage import FileStorage
        cls.base_model1 = BaseModel()
        cls.file_storage1 = FileStorage()

    @classmethod
    def tearDown(cls):
        """Cleans up after each test.
        """
        del cls.base_model1
        del cls.file_storage1

    def test_class_exists(self):
        """Tests if class exists.
        """
        result = "<class 'models.engine.file_storage.FileStorage'>"
        self.assertEqual(str(type(self.file_storage1)), result)

    def test_types(self):
        """Test if attributes type is correct.
        """
        from models.engine.file_storage import FileStorage
        self.assertIsInstance(self.file_storage1, FileStorage)
        self.assertEqual(type(self.file_storage1), FileStorage)

    def test_functions(self):
        """Test if FileStorage module is documented.
        """
        from models import storage
        from models.engine.file_storage import FileStorage
        self.assertIsNotNone(FileStorage.__doc__)

    def test_save(self):
        """Test if save method is working correctly.
        """
        from models import storage
        self.file_storage1.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload(self):
        """Tests if reload method is working correctly.
        """
        from models import storage
        from models.engine.file_storage import FileStorage
        self.base_model1.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())


if __name__ == '__main__':
    unittest.main()
