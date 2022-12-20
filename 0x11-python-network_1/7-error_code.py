#!/usr/bin/python3
"""manage and handle exceptions"""
if __name__ == "__main__":
    import requests
    import sys
    response = requests.get(sys.argv[1])
    if response.status_code == 200:
        print(response.text)
    elif response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
