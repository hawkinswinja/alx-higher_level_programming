#!/usr/bin/python3
"""make a post request using http"""
if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse
    mail = sys.argv[2]
    data = {"email": mail}
    url = sys.argv[1]
    encoded_data = urllib.parse.urlencode(data)
    data = encoded_data.encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        text = response.read()
    print(text.decode('utf-8'))
