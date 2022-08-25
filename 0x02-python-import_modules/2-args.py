#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
        sys.exit()
    if argc == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
        sys.exit()
    if argc > 2:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{}: {}".format(i, sys.argv[i]))
        sys.exit()
