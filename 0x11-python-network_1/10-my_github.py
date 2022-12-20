#!/usr/bin/python3
"""use basic authentiction to access credentials"""
if __name__ == "__main__":
    import requests
    import sys
    uri = "https://api.github.com/user"
    response = requests.get(uri, auth=(sys.argv[1], sys.argv[2]))
    data = response.json()
    print(data.get('id'))
