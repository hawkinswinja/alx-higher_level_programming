#!/usr/bin/python3
"""test cases for rectangle instances"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """test case functions for class Rectangle instances"""
    def test_subclass(self):
        """check rectangle is a subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_id(self):
        """tests for id creation from Baseclass"""
        r1 = Rectangle(10, 2, 0, 0, 3)
        self.assertEqual(r1.id, 3)

    def test_selfid(self):
        """tests for id creation without args for id"""
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, r2.id)

    def test_idincrement(self):
        """self increment for instances without id"""
        rec1 = Rectangle(4, 5)
        self.assertEqual(rec1.id, rec1.id)
        rec2 = Rectangle(10, 8)
        self.assertEqual(rec2.id, rec1.id + 1)

    def test_width_typeerror(self):
        """raise typeerror if width is not int"""
        with self.assertRaises(TypeError):
            Rectangle("a", 2)

    def test_type_height(self):
        """raise typeerror if height is not int"""
        with self.assertRaises(TypeError):
            Rectangle(10, [])

    def test_type_x(self):
        """raise typeerror if x is not int"""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 'a')

    def test_type_y(self):
        """raise typeerror if y is not int"""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 4, 'a')

    def test_value_width(self):
        """raise valueerror if width = 0"""
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_value_x(self):
        """raise valueerror if x < 0"""
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -6, 2)

    def test_value_height(self):
        """raise valueeerror if height <= 0"""
        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_value_y(self):
        """raise valueerror if x < 0"""
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 6, -2)

    def test_get_width(self):
        """returns the value of width"""
        a = Rectangle(2, 3)
        self.assertEqual(a.width, 2)

    def test_get_height(self):
        """returns the value of height"""
        a = Rectangle(2, 3)
        self.assertEqual(a.height, 3)

    def test_get_x(self):
        """returns the value of x"""
        a = Rectangle(2, 3)
        self.assertEqual(a.x, 0)

    def test_get_y(self):
        """returns the value of y"""
        a = Rectangle(2, 3)
        self.assertEqual(a.y, 0)

    def test_set_width(self):
        """sets the value of width"""
        a = Rectangle(2, 3)
        a.width = 5
        self.assertEqual(a.width, 5)

    def test_set_height(self):
        """sets the value of height"""
        a = Rectangle(2, 3)
        a.height = 1
        self.assertEqual(a.height, 1)

    def test_set_x(self):
        """sets the value of x"""
        a = Rectangle(2, 3)
        a.x = 4
        self.assertEqual(a.x, 4)

    def test_set_y(self):
        """returns the value of y"""
        a = Rectangle(2, 3)
        a.y = 2
        self.assertEqual(a.y, 2)

    def test_area(self):
        """test the area function result"""
        a = Rectangle(2, 3)
        self.assertEqual(a.area(), 6)

    def test__str__(self):
        """test the print area of rectangle"""
        a = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(a), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """test the update function"""
        a = Rectangle(4, 6, 2, 1, 12)
        a.update(10)
        self.assertEqual(a.id, 10)
