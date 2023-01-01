#!/usr/bin/python3
"""request content headers from http response"""
if __name__ == "__main__":
    import requests
    import sys
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
