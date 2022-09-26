#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""class square that inherits from rectangle"""


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
