#!/usr/bin/python3
"""This module defines tests for the BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_instance(self):
        """Test that BaseModel creates a valid instance"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_is_string(self):
        """Test that id is a string"""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_id_is_unique(self):
        """Test that two instances have different ids"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object"""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object"""
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        """Test the string representation of BaseModel"""
        obj = BaseModel()
        expected = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected)

    def test_save(self):
        """Test that save updates updated_at"""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test that to_dict returns a dictionary"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_has_class(self):
        """Test that to_dict contains __class__ key"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIn("__class__", obj_dict)

    def test_to_dict_dates_are_strings(self):
        """Test that dates in to_dict are strings"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
