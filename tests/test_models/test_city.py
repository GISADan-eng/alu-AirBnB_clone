#!/usr/bin/python3
"""This module defines tests for the City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_instance(self):
        """Test that City creates a valid instance"""
        obj = City()
        self.assertIsInstance(obj, City)

    def test_name(self):
        """Test that name is a string"""
        obj = City()
        self.assertIsInstance(obj.name, str)

    def test_state_id(self):
        """Test that state_id is a string"""
        obj = City()
        self.assertIsInstance(obj.state_id, str)


if __name__ == "__main__":
    unittest.main()
