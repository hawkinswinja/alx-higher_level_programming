#!/usr/bin/python3
"""this module defines class student with one function"""


class Student:
    """class representation of student details"""

    def __init__(self, first_name, last_name, age):
        """initialization of public variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves the json dict of the student"""
        if type(attrs) is list and len(attrs) != 0:
            nlist = []
            for attr in attrs:
                x = self.__dict__.get(attr)
                if x is not None:
                    nlist.append((attr, x))
            return dict(nlist)
        else:
            return self.__dict__
