#!/usr/bin/python3
"""Contains top_ten"""
import requests


def top_ten(subreddit):
    """Print the titles of 10 hottest posts on a subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced (by /u/IllBuilder2529)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    top = response.json().get("data")
    [print(c.get("data").get("title")) for c in top.get("children")]
