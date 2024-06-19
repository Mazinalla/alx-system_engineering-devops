#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API to retrieve the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): A list to store the titles of hot articles. Defaults to an empty list.
        after (str, optional): A token indicating the starting point for the next page of results. Defaults to None.

    Returns:
        list: A list containing the titles of all hot articles for the subreddit.
              Returns None if the subreddit is invalid or no results are found.
    """
    # Base URL for Reddit API hot posts endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Parameters for the GET request
    params = {
        'limit': 100,  # Maximum number of posts per request
        'after': after  # Token for the next page of results
    }

    # Custom headers with User-Agent to avoid 'Too Many Requests' error
    headers = {
        "User-Agent": "MyRedditClient/0.1"
    }

    try:
        # Make a GET request to Reddit API
        response = requests.get(url, params=params, headers=headers, allow_redirects=False)

        # Check if the response status code is 200 (success)
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            posts = data['data']['children']

            # Extract titles and append to hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # Check if there is a next page (pagination)
            after = data['data'].get('after')
            
            # Recursively call recurse function if there is a next page
            if after:
                recurse(subreddit, hot_list, after)

            # Return the hot_list once all pages are fetched
            return hot_list
        else:
            # If status code is not 200, return None (subreddit may be invalid)
            return None

    except Exception as e:
        # Print the exception (for debugging purposes)
        print(f"An error occurred: {e}")
        return None

