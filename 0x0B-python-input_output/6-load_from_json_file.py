#!/usr/bin/python3
""" json deserialization of string objects from file"""
import json


def load_from_json_file(filename):
    """ serialization of objects in file
        @args:
            filename(name of file)
    """
    with open(filename, 'r', encoding='utf-8') as f:
       x = json.load(f)
    return x
