#!/usr/bin/python3
"""  write contents to end of file"""


def append_write(filename="", text=""):
    """add content to end of file
        @args:
            filename(file to read from)
    """
    with open(filename, 'a', encoding='utf-8') as f:
        n = f.write(text)
    return n
