#!/usr/bin/python3
"""This module defines tests for the User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def test_instance(self):
        """Test that User creates a valid instance"""
        obj = User()
        self.assertIsInstance(obj, User)

    def test_email(self):
        """Test that email is a string"""
        obj = User()
        self.assertIsInstance(obj.email, str)

    def test_password(self):
        """Test that password is a string"""
        obj = User()
        self.assertIsInstance(obj.password, str)

    def test_first_name(self):
        """Test that first_name is a string"""
        obj = User()
        self.assertIsInstance(obj.first_name, str)

    def test_last_name(self):
        """Test that last_name is a string"""
        obj = User()
        self.assertIsInstance(obj.last_name, str)


if __name__ == "__main__":
    unittest.main()
