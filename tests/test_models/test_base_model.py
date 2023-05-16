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

    def test_class_exists(self):
        """
        Tests if class exists.
        """
        result = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(self.BaseModel1)), result)

    def testBaseModel1(self):
        """
        Test attributes value of a BaseModel instance.
        """
        self.BaseModel1.save()
        my_model_json = self.BaseModel1.to_dict()

        self.assertEqual(self.BaseModel1.name, my_model_json['name'])
        self.assertEqual(self.BaseModel1.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.BaseModel1.id, my_model_json['id'])

    def test_types(self):
        """
        Test if attributes type is correct.
        """
        self.assertIsInstance(self.BaseModel1.name, str)
        self.assertEqual(type(self.BaseModel1.name), str)
        self.assertIsInstance(self.BaseModel1.id, str)
        self.assertEqual(type(self.BaseModel1.id), str)
        self.assertIsInstance(self.BaseModel1.created_at, datetime.datetime)
        self.assertIsInstance(self.BaseModel1.updated_at, datetime.datetime)

    def test_functions(self):
        """
        Test if BaseModel moudule is documented.
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_has_attributes(self):
        """
        Test if expected attributes exist.
        """
        self.assertTrue(hasattr(self.BaseModel1, 'name'))
        self.assertTrue(hasattr(self.BaseModel1, 'id'))
        self.assertTrue(hasattr(self.BaseModel1, 'created_at'))
        self.assertTrue(hasattr(self.BaseModel1, 'updated_at'))

    def test_set_attributes(self):
        """
        Test set attributes of BaseModel.
        """
        self.assertEqual(self.BaseModel1.name, "Samsung")
        self.assertEqual(self.BaseModel1.my_number, 89)

    def test_to_dict(self):
        """
        Test if to_dict method is working correctly.
        """
        my_model_json = self.BaseModel1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.BaseModel1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.BaseModel1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.BaseModel1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.BaseModel1.id)

    def test_unique_id(self):
        """
        Test if each instance is created with a unique ID.
        """
        basemodel2 = self.BaseModel1.__class__()
        basemodel3 = self.BaseModel1.__class__()
        basemodel4 = self.BaseModel1.__class__()
        self.assertNotEqual(self.BaseModel1.id, basemodel2.id)
        self.assertNotEqual(self.BaseModel1.id, basemodel3.id)
        self.assertNotEqual(self.BaseModel1.id, basemodel4.id)

    def test__str__(self):
        """
        Test if __str__ method returns expected string.
        """
        string = str(self.BaseModel1)
        id_test = "[BaseModel] ({})".format(self.BaseModel1.id)
        boolean = id_test in string
        self.assertEqual(True, boolean)
        boolean = "updated_at" in string
        self.assertEqual(True, boolean)
        boolean = "created_at" in string
        self.assertEqual(True, boolean)
        boolean = "datetime.datetime" in string
        self.assertEqual(True, boolean)


if __name__ == '__main__':
    unittest.main()
