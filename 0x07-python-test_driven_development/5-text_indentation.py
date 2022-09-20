#!/usr/bin/python3
"""
    text indentation module
    usage: text_indentation(text)
"""


def text_indentation(text):
    """
        replace all occurences of . : ? with nextline
        @Args:
            text(str)
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace(". ", ".\n")
    text = text.replace("? ", "?\n")
    text = text.replace(": ", ":\n")
    text = text.replace(".", ".\n")
    text = text.replace("?", "?\n")
    text = text.replace(":", ":\n")
    print(text, end='')
