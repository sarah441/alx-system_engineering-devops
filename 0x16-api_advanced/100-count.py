#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """ A function that prints a sorted count of given keywords."""

    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        wordict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for w in wordict:
            if w[1]:
                print('{}: {}'.format(w[0], w[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'IllBuilder2529'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hposts = response.json()['data']['children']
        aftt = response.json()['data']['after']
        for art in hposts:
            title = art['data']['title']
            lower = [w.lower() for w in title.split(' ')]

            for w in word_dict.keys():
                word_dict[w] += lower.count(w)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dict)
