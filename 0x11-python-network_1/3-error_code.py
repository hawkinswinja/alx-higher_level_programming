#!/usr/bin/python3
"""handling http errors"""
import sys
import urllib.request
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except Exception as e:
        print("Error code: {}".format(e.code))
