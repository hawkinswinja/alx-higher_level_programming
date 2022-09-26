#!/usr/bin/python3
"""4-inherits_from.py module
   usage: inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """checks if the object inherits from a_class
       @args:
             obj(an object of type class)
             a_class(an object of type class)
       returns True if obj inherits from a_class
    """
    if issubclass(type(obj), a_class):
        return True
    return False

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
