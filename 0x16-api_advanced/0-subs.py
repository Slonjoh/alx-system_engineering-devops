#!/usr/bin/python3
"""Function to query subscribers on Reddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Uses the reddit api to get the numbers of subscribers to a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
