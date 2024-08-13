#!/usr/bin/python3
"""
To know the count of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """to handle errors"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    about = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
                             v1.0.0 (by /u/IllBuilder2529)'}).json()
    subs_count = about.get("data", {}).get("subscribers", 0)
    return subs_count
