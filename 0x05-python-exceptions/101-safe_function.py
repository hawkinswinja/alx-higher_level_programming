#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    c = None
    if fct and args:
        try:
            c = fct(args[0], args[1])
        except ZeroDivisionError as err:
            print("Exception: ", err, file=sys.stderr)
        except ValueError as err:
            print("Exception: ", err, file=sys.stderr)
        except IndexError as err:
            print("Exception: ", err, file=sys.stderr)
    return c
