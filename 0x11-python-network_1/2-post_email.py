#!/usr/bin/python3.4
"""Script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    if (argv[1] is not None and argv[2] is not None):
        url = argv[1]
        email = argv[2]
        values = {'email': email}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')  # data should be bytes
        with urllib.request.urlopen(url, data) as response:
            body = response.read()
            body = body.decode("UTF-8")
            print(body)
