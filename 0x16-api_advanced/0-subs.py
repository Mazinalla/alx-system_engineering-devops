import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API to get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers to the subreddit. Returns 0 if the subreddit
             is invalid or if an error occurs.
    """
    # Set the base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set custom headers, including a User-Agent to avoid 'Too Many Requests' error
    headers = {
        "User-Agent": "MyRedditClient/0.1"
    }

    try:
        # Make a GET request to the subreddit's JSON endpoint
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code indicates success
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the status code is not 200, return 0
            return 0
    except Exception:
        # If there is any exception (e.g., network error), return 0
        return 0

