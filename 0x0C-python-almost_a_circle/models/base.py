#!/usr/bin/python3
"""class module definition of a base class"""


class Base:
    """class to manage attributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantialize variables"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
