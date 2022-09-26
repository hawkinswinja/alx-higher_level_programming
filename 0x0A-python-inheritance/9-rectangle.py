#!/usr/bin/python3
""" 9-base_geometry module
    class with defined function
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creates a  class rectangle"""
    def area(self):
        """returns the area of the rectangle"""
        return self.__width__ * self.__height__

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
