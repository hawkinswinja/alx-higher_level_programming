#!/usr/bin/python3
""" json deserialization of string objects"""
import json


def from_json_string(my_str):
    """ deserialization of object my_str
        @args:
            my_str(string serialized object)
    """
    return json.loads(my_str)
