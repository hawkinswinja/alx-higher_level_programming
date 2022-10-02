#!/usr/bin/python3
"""square module that inherits from rectangle"""
from rectangle import Rectangle


class Square(Rectangle):
    """defines the shape square and area"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the dimensions of the square and instance id"""
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y

    @property
    def size(self):
        """returns the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """update the value of size"""
        Rectangle(value, value, self.__x, self.__y, self.id)

    def __str__(self):
        """returns the description of the square"""
        x = str(self.__x) + "/"
        y = str(self.__y) + " - "
        size = str(self.__size)
        iid = " (" + str(self.id) + ") "
        return "[Square]" + iid + x + y + size

    def update(self, *args, **kwargs):
        """update attributes of the square"""
        n = len(args)
        if n > 0:
            self.id = args[0]
        if n > 1:
            self.__size = args[1]
        if n > 2:
            self.__x = args[2]
        if n > 3:
            self.__y = args[3]
        if n == 0 and kwargs is not None:
            mydict = {"id": self.id, "size": self.__size}
            dict2 = {"x": self.__x, "y": self.__y}
            mydict.update((k, v) for k, v in kwargs.items())
            dict2.update((k, v) for k, v in kwargs.items())
            self.id = mydict.get("id")
            self.__size = mydict.get("size")
            self.__x = dict2.get("x")
            self.__y = dict2.get("y")

    def to_dictionary(self):
        """returns the dictionary rep instance"""
        mydict = {"x": self.__x, "y": self.__y,
                  "id": self.id, "size": self.__size}
        return mydict
