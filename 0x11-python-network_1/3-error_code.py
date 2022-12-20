#!/usr/bin/python3
"""handling http errors"""
import sys
import urllib.request
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read())
    except Exception as e:
        errorcode = str(e).split()[2].split(':')[0]
        print("Error code: {}".format(errorcode))
