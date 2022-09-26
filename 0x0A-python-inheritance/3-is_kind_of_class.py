#!/usr/bin/python3
"""3-is_kind_of_class.py module
   usage: is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """checks if the object is of type a_class
       @args:
             obj(an object of any type)
             a_class(anobject of type class)
       returns True if obj is of type a_class
    """
    if isinstance(obj, a_class):
        return True
    return False
