#!/usr/bin/python3
"""post content headers to http server"""
if __name__ == "__main__":
    import requests
    import sys
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
