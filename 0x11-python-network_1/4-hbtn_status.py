#!/usr/bin/python3.4
"""Sccript that fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    content = r.text
    print("Body response:")
    print("\t- type: " + str(type(content)))
    print("\t- content: " + str(content))
    