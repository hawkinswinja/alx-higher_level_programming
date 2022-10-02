#!/usr/bin/python3
"""square module that inherits from rectangle"""
from rectangle import Rectangle


class Square(Rectangle):
    """defines the shape square and area"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the dimensions of the square and instance id"""
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y

    @property
    def size(self):
        """returns the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """update the value of size"""
        Rectangle(value, value, self.__x, self.__y, self.id)

    def __str__(self):
        """returns the description of the square"""
        x = str(self.__x) + "/"
        y = str(self.__y) + " - "
        size = str(self.__size)
        iid = " (" + str(self.id) + ") "
        return "[Square]" + iid + x + y + size
