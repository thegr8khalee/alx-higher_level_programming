#!/usr/bin/python3
"""that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response."""

import urllib.request
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(dict(response.headers).get("X-Request-Id"))
    except Exception as e:
        print(e)
