#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
            html = response.read()
    except Exception as e:
        print(e)

    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode("utf-8")))
