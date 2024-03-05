#!/usr/bin/python3
import requests
import sys
"""
Module to interface with the reddit api
"""


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Uses the reddit api to get a count of search terms from subreddit hot posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Custom User-Agent to prevent Too Many Requests error
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']

        for child in children:
            title = child['data']['title']
            words = title.lower().split()
            for word in word_list:
                word = word.lower()
                if word in words:
                    if word in counts:
                        counts[word] += words.count(word)
                    else:
                        counts[word] = words.count(word)

        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or no posts match.")
