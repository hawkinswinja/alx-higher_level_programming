#!/usr/bin/python3
"""0-lookup module
   usage:lookup(obj)
"""


def lookup(obj):
    """function to list all objects and methods
       @args:
            obj(object of any type)
    """
    return (list(obj.__dict__))
