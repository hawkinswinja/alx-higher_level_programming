#!/usr/bin/python3
""" json serialization of string objects to file"""
import json


def save_to_json_file(my_obj, filename):
    """ deserialization of object my_str
        @args:
            my_str(string serialized object)
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
