#!/usr/bin/python3.4
"""Script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 2:
        user = argv[1]
        token = argv[2]
        query_url = "https://api.github.com/users/{}".format(user)
        params = {
            "state": "open",
        }
        headers = {'Authorization': 'token {}'.format(token)}
        r = requests.get(query_url, headers=headers, params=params)
        j = r.json()
        print(j.get("id"))
