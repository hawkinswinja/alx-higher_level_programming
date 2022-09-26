#!/usr/bin/python3
""" 9-base_geometry module
    class with defined function
"""


class Rectangle:
    """creates a  class rectangle"""
    def area(self):
        """returns the area of the rectangle"""
        return self.__width__ * self.__height__

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

    def __str__(self):
        """description of the rectangle
           defined for user consumption
        """
        width = str(self.__width__)
        height = str(self.__height__)
        return ("[Rectangle] " + width + "/" + height)
