#!/usr/bin/python3
"""add text after a searched line"""


def append_after(filename="", search_string="", new_string=""):
    """append text after searching in line"""
    list_line = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            list_line.append(line)
            if line.find(search_string) != -1:
                list_line.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("".join(list_line))
