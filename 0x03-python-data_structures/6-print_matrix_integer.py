#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for i in a:
            print("{:d}".format(i), end='')
            if i == a[-1]:
                break
            print(" ", end='')
        print("")
