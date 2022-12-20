#!/usr/bin/python3
"""post  and request json params"""
if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv < 2):
        q = ''
    q = sys.argv[1]
    response = requests.post("http://0.0.0.0:5000", data={"q": q})
    try:
        r = response.json()
        if r == {}:
            print("No result")
        else:
            print("{}: {}".format(r['id'], r['name']))
    except ValueError:
        print("Not a valid JSON")
