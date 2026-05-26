#!/usr/bin/python3
"""This module defines tests for the Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def test_instance(self):
        """Test that Place creates a valid instance"""
        obj = Place()
        self.assertIsInstance(obj, Place)

    def test_name(self):
        """Test that name is a string"""
        obj = Place()
        self.assertIsInstance(obj.name, str)

    def test_city_id(self):
        """Test that city_id is a string"""
        obj = Place()
        self.assertIsInstance(obj.city_id, str)

    def test_number_rooms(self):
        """Test that number_rooms is an int"""
        obj = Place()
        self.assertIsInstance(obj.number_rooms, int)

    def test_price_by_night(self):
        """Test that price_by_night is an int"""
        obj = Place()
        self.assertIsInstance(obj.price_by_night, int)


if __name__ == "__main__":
    unittest.main()
