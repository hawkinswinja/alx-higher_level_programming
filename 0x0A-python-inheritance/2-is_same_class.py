#!/usr/bin/python3
"""2-is_same_class.py module
   usage: is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """checks if the object is of type a_class
       @args:
             obj(an object of any type)
             a_class(anobject of type class)
       returns True if obj is of type a_class
    """
    if type(obj) is a_class:
        return True
    return False
