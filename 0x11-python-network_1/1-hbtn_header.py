#!/usr/bin/python3
"""return the X-request-Id variable from header response"""
if __name__ == "__main__":
    import sys
    import urllib.request
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        headers = dict(resp.headers)
    print(headers['X-Request-Id'])
