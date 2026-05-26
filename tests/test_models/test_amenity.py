#!/usr/bin/python3
"""This module defines tests for the Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_instance(self):
        """Test that Amenity creates a valid instance"""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_name(self):
        """Test that name is a string"""
        obj = Amenity()
        self.assertIsInstance(obj.name, str)


if __name__ == "__main__":
    unittest.main()
