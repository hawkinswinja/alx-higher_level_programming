#!/usr/bin/python3
""" read file contents and print"""


def read_file(filename=""):
    """ prints to stdout
        @args:
            filename(file to read from)
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
