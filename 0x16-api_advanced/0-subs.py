#!/usr/bin/python3
"""
Reddit API Utility Module

This module provides a function to query the Reddit API and get the number of
subscribers for a given subreddit. If an invalid subreddit is given, the 
function will return 0.

Functions:
    number_of_subscribers(subreddit): Returns the number of subscribers for
                                      the given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Query the Reddit API to get the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers. Returns 0 if the subreddit is invalid.
    """
    # Construct the URL for the subreddit's about page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set a custom User-Agent
    headers = {'User-Agent': 'my-app/0.0.1'}
    
    try:
        # Make a GET request to the URL
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check the status code of the response
        if response.status_code == 200:
            # Parse the JSON data to get the number of subscribers
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the status code is not 200, return 0 (invalid subreddit)
            return 0
    except requests.RequestException:
        # Handle any potential exceptions and return 0
        return 0
