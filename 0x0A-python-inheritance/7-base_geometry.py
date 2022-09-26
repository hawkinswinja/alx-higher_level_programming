#!/usr/bin/python3
""" 7-base_geometry module
    class with defined function
"""


class BaseGeometry:
    """creates a  class"""
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
