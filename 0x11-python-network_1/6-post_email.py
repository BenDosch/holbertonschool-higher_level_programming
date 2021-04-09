#!/usr/bin/python3.4
"""Script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays
the body of the response."""
from sys import argv
import requests


if __name__ == "__main__":
    if argv[1] is not None and argv[2] is not None:
        url = argv[1]
        email = argv[2]
        data = {'email': email}
        r = requests.post(url, data)
        body = r.text
        print(str(body))
