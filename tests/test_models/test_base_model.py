#!/usr/bin/python3
"""unit tests for base model module"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel"""

    def setUp(self):
        """create instance"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Delete instance"""
        del self.base_model

    def test_instance_attributes(self):
        """Test instance attributes"""
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))
        self.assertEqual(self.base_model.__class__.__name__, "BaseModel")

    def test_id_type(self):
        """Test if id is of type string"""
        self.assertEqual(type(self.base_model.id), str)

    def test_created_at_type(self):
        """Test if created_at is of type datetime"""
        self.assertEqual(type(self.base_model.created_at), datetime.datetime)

    def test_updated_at_type(self):
        """Test if updated_at is of type datetime"""
        self.assertEqual(type(self.base_model.updated_at), datetime.datetime)

    def test_to_dict(self):
        """Test to_dict method"""
        dict_ = self.base_model.to_dict()
        self.assertEqual(dict_["__class__"], "BaseModel")
        self.assertEqual(type(dict_["created_at"]), str)
        self.assertEqual(type(dict_["updated_at"]), str)

    def test_str_method(self):
        """Test __str__ method"""
        string = str(self.base_model)
        self.assertEqual("[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__), string)

    def test_save_method(self):
        """Test save method"""
        self.base_model.save()
        self.assertNotEqual(self.base_model.created_at,
                            self.base_model.updated_at)
