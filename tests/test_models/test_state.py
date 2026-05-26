#!/usr/bin/python3
"""This module defines tests for the State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def test_instance(self):
        """Test that State creates a valid instance"""
        obj = State()
        self.assertIsInstance(obj, State)

    def test_name(self):
        """Test that name is a string"""
        obj = State()
        self.assertIsInstance(obj.name, str)


if __name__ == "__main__":
    unittest.main()
