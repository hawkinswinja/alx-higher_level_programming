#!/usr/bin/python3
""" 8-base_geometry module
    class with defined function
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creates a  class rectangle that inherits from BaseGeometry"""

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
