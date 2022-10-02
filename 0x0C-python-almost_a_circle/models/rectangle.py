#!/usr/bin/python3
"""class rectanlge module"""
from base import Base


class Rectangle(Base):
    """class that defines the rectangle and intializes on instance"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize on instance"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """returns the value of private variable width"""
        return self.__width

    @width.setter
    def width(self, value):
        """update the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the value of private variable height"""
        return self.__height

    @height.setter
    def height(self, value):
        """update the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the value of private variable x"""
        return self.__x

    @x.setter
    def x(self, value):
        """update the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns the value of private variable y"""
        return self.__y

    @y.setter
    def y(self, value):
        """update the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the area of the rectangle using #"""
        for i in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """rectangle description in dimensions"""
        x = str(self.__x)
        y = str(self.__y)
        width = str(self.__width)
        height = str(self.__height)
        iid = " (" + str(self.id) + ") "
        return "[Rectangle]" + iid + x + "/" + y + " - " + width + "/" + height

    def update(self, *args, **kwargs):
        """updates the variables of the rectangle"""
        n = len(args)
        if n > 0:
            self.id = args[0]
        if n > 1:
            self.__width = args[1]
        if n > 2:
            self.__height = args[2]
        if n > 3:
            self.__x = args[3]
        if n > 4:
            self.__y = args[4]
        if n == 0 and kwargs is not None:
            mydict = {"id": self.id, "width": self.__width}
            mydict2 = {"x": self.__x, "y": self.__y, "height": self.__height}
            mydict.update((k, v) for k, v in kwargs.items())
            self.id = mydict.get("id")
            mydict2.update((k, v) for k, v in kwargs.items())
            self.__width = mydict.get("width")
            self.__height = mydict2.get("height")
            self.__x = mydict2.get("x")
            self.__y = mydict2.get("y")

    def to_dictionary(self):
        """returns the dictionary rep of instance"""
        mydict = {"x": self.__x, "y": self.__y, "id": self.id,
                  "height": self.__height, "width": self.__width}
        return mydict

if __name__ == "__main__":
    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
