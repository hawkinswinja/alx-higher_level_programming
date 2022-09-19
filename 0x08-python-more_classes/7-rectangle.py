#!/usr/bin/python3
"""class rectangle that defines a rectangle"""


class Rectangle:
    """class defining a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ intializes lenght and width"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """update size of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """update height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """print the rectangle"""
        if self.perimeter == 0:
            print("")
            return
        else:
            mylist = []
            for i in range(0, self.__height):
                mylist.append(Rectangle.print_symbol * self.__width)
            return "\n".join(mylist)

    def __repr__(self):
        """allows for the creation of another instance"""
        a = 'Rectangle(' + str(self.__width) + ', ' + str(self.__height) + ')'
        return a

    def __del__(self):
        """delete the current instance"""
        print("Bye rectangle ...")
        Rectangle.number_of_instances -= 1
