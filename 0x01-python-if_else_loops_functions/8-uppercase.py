#!/usr/bin/python3
def uppercase(str):
    "UPPERCASE GIVEN STRING"
    for i in range(len(str)):
        temp = ord(str[i])
        if temp in range(97, 123):
            temp = temp - 32
        print("{}".format(chr(temp)), end='')
    print()
