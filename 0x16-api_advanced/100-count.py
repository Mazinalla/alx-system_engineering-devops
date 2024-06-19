#!/usr/bin/python3
import requests
import re
from collections import defaultdict
from operator import itemgetter

def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively query the Reddit API to count occurrences of specified keywords in hot article titles.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count occurrences in titles.
        after (str, optional): A token indicating the starting point for the next page of results. Defaults to None.
        word_counts (defaultdict(int), optional): A dictionary to store word counts. Defaults to None.

    Returns:
        None
    """
    if word_counts is None:
        word_counts = defaultdict(int)

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

            # Extract titles and update word counts
            for post in posts:
                title = post['data']['title']
                # Split title into words using regex (non-alphanumeric characters as delimiters)
                words = re.findall(r'\w+', title.lower())
                # Count occurrences of words in word_list
                for word in word_list:
                    if word.lower() in words:
                        word_counts[word.lower()] += words.count(word.lower())

            # Check if there is a next page (pagination)
            after = data['data'].get('after')

            # Recursively call count_words function if there is a next page
            if after:
                count_words(subreddit, word_list, after, word_counts)
            else:
                # Once all pages are fetched, print results sorted by count (descending) and word (ascending)
                sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")

        else:
            # If status code is not 200, print nothing (subreddit may be invalid)
            print(None)

    except Exception as e:
        # Print the exception (for debugging purposes)
        print(f"An error occurred: {e}")

