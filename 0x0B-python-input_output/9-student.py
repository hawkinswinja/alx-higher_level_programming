#!/usr/bin/python3
"""this module defines class student with one function"""


class Student:
    """class representation of student details"""

    def __init__(self, first_name, last_name, age):
        """initialization of public variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the json dict of the student"""
        return self.__dict__
