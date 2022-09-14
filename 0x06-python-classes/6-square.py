#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""


class Square:
    """ python3 -c 'print(__import__("my_module").MyClass.__doc__)'
        Private instance attribute size. size of the square."""
    def __init__(self, size=0, position=(0, 0)):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
           python3 -c 'print(__import__("my_module").\
           MyClass.my_function.__doc__)'
           initialize size and position."""
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
           python3 -c 'print(__import__("my_module").\
           MyClass.my_function.__doc__)'
           returns position."""
        return self.__position

    @position.setter
    def position(self, value):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
           python3 -c 'print(__import__("my_module").\
           MyClass.my_function.__doc__)'
           update values of position."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
                print(' ' * self.__position[0] + '#' * self.__size)
