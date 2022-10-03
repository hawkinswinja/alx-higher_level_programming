#!/usr/bin/python3
"""test cases for square instances"""
import unittest
from models.square import Square
from models.base import Base


class TestRectangle(unittest.TestCase):
    """test case functions for class Rectangle instances"""
    def test_subclass(self):
        """check rectangle is a subclass of Rectangle"""
        self.assertTrue(issubclass(Square, Base))

    def test_id(self):
        """tests for id creation from Baseclass"""
        s1 = Square(10, 2, 3, 3)
        self.assertEqual(s1.id, 3)

    def test_selfid(self):
        """tests for id creation without args for id"""
        s2 = Square(10)
        self.assertFalse(s2.id is None)

    def test_idincrement(self):
        """self increment for instances without id"""
        sq1 = Square(4)
        self.assertFalse(sq1.id is None)
        sq2 = Square(10)
        self.assertEqual(sq2.id, sq1.id + 1)

    def test_size_typeerror(self):
        """raise typeerror if size is not int"""
        with self.assertRaises(TypeError):
            Square("a")

    def test_type_x(self):
        """raise typeerror if x is not int"""
        with self.assertRaises(TypeError):
            Square(10, 'a', 3)

    def test_type_y(self):
        """raise typeerror if y is not int"""
        with self.assertRaises(TypeError):
            Square(10, 5, 'a')

    def test_value_size(self):
        """raise valueerror if size <= 0"""
        with self.assertRaises(ValueError):
            Square(-2)

    def test_value_x(self):
        """raise valueerror if x < 0"""
        with self.assertRaises(ValueError):
            Square(10, -5, 2)

    def test_value_y(self):
        """raise valueeerror if y < 0"""
        with self.assertRaises(ValueError):
            Square(10, 4, -5)

    def test_get_size(self):
        """returns the size of the square"""
        a = Square(2, 3, 4)
        self.assertEqual(a.size, 2)

    def test_get_x(self):
        """returns the value of x"""
        a = Square(2, 3, 4)
        self.assertEqual(a.x, 3)

    def test_get_y(self):
        """returns the value of y"""
        a = Square(2, 3, 4)
        self.assertEqual(a.y, 4)

    def test_set_size(self):
        """sets the value of width"""
        a = Square(2, 3, 4, 12)
        a.size = 5
        self.assertEqual(a.size, 5)

    def test__init__(self):
        """sets the value of height"""
        a = Square(2)
        self.assertEqual(a.height, a.size)
        self.assertEqual(a.width, a.size)

    def test_set_x(self):
        """sets the value of x"""
        a = Square(2, 3, 4)
        a.x = 22
        self.assertEqual(a.x, 22)

    def test_set_y(self):
        """returns the value of y"""
        a = Square(2, 3, 4)
        a.y = 2
        self.assertEqual(a.y, 2)

    def test_area(self):
        """test the area function result"""
        a = Square(4)
        self.assertEqual(a.area(), 16)

    def test__str__(self):
        """test the print area of rectangle"""
        new = Square(5)
        rep = "[Square] (" + str(new.id) + ") 0/0 - 5"
        self.assertEqual(str(new), rep)

    def test_update(self):
        """test the update function"""
        a = Square(5)
        a.update(10)
        self.assertEqual(a.id, 10)
