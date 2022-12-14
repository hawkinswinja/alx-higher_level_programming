#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    if value:
        try:
            print("{:d}".format(value))
            return True
        except ValueError as err:
            print("Exception: {}".format(err), file=sys.stderr)
