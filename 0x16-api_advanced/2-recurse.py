#!/usr/bin/python3
import requests
"""
Module to interface with the reddit api
"""


def recurse(subreddit, after=None, all_results=[]):
    """
    Uses the reddit api to get the numbers of hot posts in a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for child in children:
            hot_list.append(child['data']['title'])
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
