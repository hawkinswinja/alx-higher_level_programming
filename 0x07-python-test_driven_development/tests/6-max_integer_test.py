#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """assert output of the list contents
    """
    def test_max_integer(self):
        """function to test expected output of function
        """
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([2.1, 2, 2.05]), 2.1)
        self.assertAlmostEqual(max_integer([-4, -2, 1]), 1)
