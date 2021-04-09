#!/usr/bin/python3.4
"""Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    r = requests.post(url, data)
    try:
        j = r.json()
        if j == {}:
            print("No result")
        else:
            print("[{}] {}".format(j["id"], j["name"]))
    except:
        print("Not a valid JSON")
