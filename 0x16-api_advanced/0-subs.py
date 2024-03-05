#!/usr/bin/python3
"""Function to query subscribers on Reddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Uses the reddit api to get the numbers of subscribers to a subreddit
    """
    subRcheck = requests.get("https://reddit.com/api/search_reddit_names.json",
                             headers={
                                 'User-Agent': 'Safari 12.1'
                             },
                             params={
                                 'exact': True,
                                 'query': subreddit
                             })
    if 'error' in subRcheck.json():
        return 0
    response = requests.get("https://reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={'User-Agent': 'Safari 12.1'})
    return response.json().get('data').get('subscribers')
