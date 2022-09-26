#!/usr/bin/python3
""" 8-base_geometry module
    class with defined function
"""


class Rectangle:
    """creates a  class rectangle"""
    def area(self):
        """raises exception when the method is called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value is an integer
           value must be greater than zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __init__(self, width, height):
        """instantialization of width and height
           @args:
                width(int): positive
                height(int): positive
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width__ = width
        self.__height__ = height
