#!/usr/bin/python3
"""
   prints a square of dimension size
   usage: print_square(size)
"""


def print_square(size):
    """
        prints a square using # unit
        Args:
            size(int) length of the square
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size, end='')
        print("")
