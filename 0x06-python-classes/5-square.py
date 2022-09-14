#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Square:
    """ python3 -c 'print(__import__("my_module").MyClass.__doc__)'
        Private instance attribute size. size of the square."""
    def __init__(self, size=0):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
           python3 -c 'print(__import__("my_module").\
           MyClass.my_function.__doc__)'
           initialize size."""
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
           python3 -c 'print(__import__("my_module").\
           MyClass.my_function.__doc__)'
           returns size."""
        return self.__size

    @size.setter
    def size(self, value):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
           python3 -c 'print(__import__("my_module").\
           MyClass.my_function.__doc__)'
           sets size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
           python3 -c 'print(__import__("my_module").\
           MyClass.my_function.__doc__)'
           Returns the Area of the square."""
        return self.__size**2

    def my_print(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
           python3 -c 'print(__import__("my_module").\
           MyClass.my_function.__doc__)'
           prints the defined square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                print('#' * self.__size)
