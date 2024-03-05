#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """
    Uses the reddit api to get the numbers of hot posts in a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for child in children:
            print(child['data']['title'])
    else:
        print("None")
