#!/usr/bin/python3
def remove_char_at(str, n):
    if n in range(len(str)):
        a = str[:n] + str[n + 1:]
    else:
        a = str
    return a
