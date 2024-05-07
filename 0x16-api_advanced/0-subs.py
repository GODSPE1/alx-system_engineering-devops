#!/usr/bin/python3
"""
This script retrieves the number of subscribers for a given subreddit using the Reddit API.
"""

import requests

def number_of_subscribers(subreddit):
    if not subreddit:
        return 0
    else:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
                
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return None

