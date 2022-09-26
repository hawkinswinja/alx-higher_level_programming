#!/usr/bin/python3
"""class square that inherits from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square is a subclass of Rectangle
        inherits all the functions
    """
    def __init__(self, size):
        """instantialization of sides of the square"""
        super().__init__(size, size)
        self.__size__ = size

    def area(self):
        """returns the area of the square using size"""
        return self.__size__ ** 2

    def __str__(self):
        """representation of square"""
        size = str(self.__size__)
        return ("[Square] " + size + "/" + size)
