#!/usr/bin/python3
""" read file contents and print"""
import json


def to_json_string(my_obj):
    """ str representation of object
        @args:
            my_obj(data object)
    """
    return json.dumps(my_obj)
