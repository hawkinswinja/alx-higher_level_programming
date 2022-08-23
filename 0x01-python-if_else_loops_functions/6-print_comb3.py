#!/usr/bin/python3
for i in range(10):
    p = i + 1
    for n in range(p, 10):
        print("{}".format(i), end='')
        print("{}".format(n), end=', ')
    if i == 7:
        break
print("{}{}".format(i+1, p+1))
