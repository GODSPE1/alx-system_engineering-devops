#!/usr/bin/python3
"""
This script retrieves the number of subscribers for a
given subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    user_agent = {'User-agent': 'Go9'}
    response = requests.get(url, allow_redirects=False, headers=user_agent)
    data = response.json()
    try:
        return data.get('data').get('subscribers')
    except Exception:
        return 0
