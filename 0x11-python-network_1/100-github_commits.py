#!/usr/bin/python3.4
"""Script that takes 2 arguments in order to solve this challenge:
*Please list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
*You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
*Print all commits by: `<sha>: <author name>` (one by line)"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 2:
        repo = argv[1]
        user = argv[2]
        query_url = ("https://api.github.com/repos/{}/{}/commits".
                     format(user, repo))
        params = {
            "per_page": 10,
            "page": 1
        }
        r = requests.get(query_url, params=params)
        j = r.json()
        for commit in j:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
