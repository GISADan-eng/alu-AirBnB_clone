#!/usr/bin/python3
"""This module defines tests for the Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_instance(self):
        """Test that Review creates a valid instance"""
        obj = Review()
        self.assertIsInstance(obj, Review)

    def test_text(self):
        """Test that text is a string"""
        obj = Review()
        self.assertIsInstance(obj.text, str)

    def test_place_id(self):
        """Test that place_id is a string"""
        obj = Review()
        self.assertIsInstance(obj.place_id, str)

    def test_user_id(self):
        """Test that user_id is a string"""
        obj = Review()
        self.assertIsInstance(obj.user_id, str)


if __name__ == "__main__":
    unittest.main()
