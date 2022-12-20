#!/usr/bin/python3
"""fetch web content and type"""
if __name__ == "__main__":
    import requests
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(response.text.__class__, response.text))
