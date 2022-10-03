#!/usr/bin/python3
"""unittesting for functions in class Base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test the Base class instances for id creation"""
    def test_nullId(self):
        """create id if not provided by user Test"""
        base1 = Base()
        self.assertEqual(base1.id, 1)

    def test_instance(self):
        """checks if id instance creation initialises"""
        base1 = Base(2)
        self.assertEqual(base1.id, 2)

    def test_to_json_string(self):
        """test the json representation returned"""
        a = [1, 2, 3, 4]
        self.assertEqual(Base.to_json_string(a), "[1, 2, 3, 4]")

    def test_from_json_string(self):
        """test if json deserialization returns accurately"""
        a = [1, 2, 3, 4]
        self.assertEqual(Base.from_json_string(str(a)), a)
