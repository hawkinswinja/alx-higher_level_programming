#!/usr/bin/python3
def no_c(my_string):
    b = ""
    for i in range(len(my_string)):
        if my_string[i] in 'cC':
            continue
        b += my_string[i]
    return b
