import requests


def top_ten(subreddit):
    """
    Query the Reddit API to get the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    # Set the base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set custom headers, including a User-Agent to avoid 'Too Many Requests' error
    headers = {
        "User-Agent": "MyRedditClient/0.1"
    }

    try:
        # Make a GET request to the subreddit's hot posts JSON endpoint
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code indicates success
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            # Print the titles of the first 10 hot posts
            for post in posts:
                print(post['data']['title'])
        else:
            # If the status code is not 200, print None
            print(None)
    except Exception:
        # If there is any exception (e.g., network error), print None
        print(None)

