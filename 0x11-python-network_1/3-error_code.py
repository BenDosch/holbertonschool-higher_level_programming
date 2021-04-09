#!/usr/bin/python3.4                                                                            
"""Script that takes in a URL, sends a request to the URL and                                   
displays the body of the response"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    if (argv[1] is not None):
        url = argv[1]
        try:
            response = urllib.request.urlopen(url)
            body = response.read()
            body = body.decode("UTF-8")
            print(body)
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
