#!/usr/bin/python3
"""This module defines tests for the FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def test_file_path(self):
        """Test that __file_path is a string"""
        obj = FileStorage()
        self.assertIsInstance(obj._FileStorage__file_path, str)

    def test_objects(self):
        """Test that __objects is a dictionary"""
        obj = FileStorage()
        self.assertIsInstance(obj._FileStorage__objects, dict)

    def test_instance(self):
        """Test that FileStorage creates a valid instance"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary"""
        obj = FileStorage()
        self.assertIsInstance(obj.all(), dict)

    def test_new(self):
        """Test that new() adds an object to __objects"""
        obj = FileStorage()
        base = BaseModel()
        obj.new(base)
        key = "{}.{}".format(type(base).__name__, base.id)
        self.assertIn(key, obj.all())

    def test_save_and_reload(self):
        """Test that save() and reload() work correctly"""
        obj = FileStorage()
        base = BaseModel()
        obj.new(base)
        obj.save()
        obj.reload()
        key = "{}.{}".format(type(base).__name__, base.id)
        self.assertIn(key, obj.all())


if __name__ == "__main__":
    unittest.main()
