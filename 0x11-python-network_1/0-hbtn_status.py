#!/usr/bin/python3.4
"""Script that fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        content = response.read()
        print("Body response:")
        print("\t- type: " + str(type(content)))
        print("\t- content: " + str(content))
        content = content.decode("UTF-8")
        print("\t- utf8 content: " + content)
