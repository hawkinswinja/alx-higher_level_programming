#!/usr/bin/python3
for i in range(122, 96, -1):
    n = i
    if n % 2 != 0:
        n = i - 32
    print("{}".format(chr(n)), end='')
