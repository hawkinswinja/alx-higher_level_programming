#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Square:
    """ python3 -c 'print(__import__("my_module").MyClass.__doc__)'
        Private class attribute size. size of the square."""
    __size = None

    def __init__(self, size=0):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
           python3 -c 'print(__import__("my_module").\
           MyClass.my_function.__doc__)'
           raises exception errors."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
           python3 -c 'print(__import__("my_module").\
           MyClass.my_function.__doc__)'
           Returns the Area of the square."""
        return self.__size**2
