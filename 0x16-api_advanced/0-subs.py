#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    try:
        response = requests.get(
            f'https://www.reddit.com/r/{subreddit}/about.json',
            headers={'User-Agent': (
                '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
                )
                }

        )
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            subs = data.get("data", {}).get("subscribers", 0)
            return subs
        else:
            return 0
    except (requests.RequestException, ValueError, KeyError):
        return 0
