#!/usr/bin/python3
"""class module definition of a base class"""
import json


class Base:
    """class to manage attributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantialize variables"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """parse the dictionary of instance"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the string dictionary to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            mylist = []
            for i in list_objs:
                mylist.append(i.to_dictionary())
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(Base.to_json_string(mylist))

    @staticmethod
    def from_json_string(json_string):
        """return the list of string"""
        if len(json_string) == 0 or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return a dummy created instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load dictionary from a file and create instances for the class"""
        filename = cls.__name__ + ".json"
        dictlist = []
        with open(filename, 'r') as f:
            x = Base.from_json_string(f.read())
        if len(x) != 0:
            for kwargs in x:
                dictlist.append(cls.create(**kwargs))
        return dictlist
