#!/usr/bin/python3
"""  write contents to file"""


def write_file(filename="", text=""):
    """ overwrite a file
        @args:
            filename(file to read from)
    """
    with open(filename, 'w', encoding='utf-8') as f:
        n = f.write(text)
    return n
