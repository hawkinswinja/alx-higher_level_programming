#!/usr/bin/python3
"""
   this module contains one function
   usage:  say_my_name(...)
"""


def say_my_name(first_name, last_name=""):
    """
        prints the first and last name
        Args:
            first_name(string)
            last_name(string)
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
