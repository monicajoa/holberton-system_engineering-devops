#!/usr/bin/python3
""" Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10
    hot posts listed for a given subreddit
    """
    headers = {'User-agent': 'monicajoa'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    get_req = requests.get(
        url,
        params={"limit": 10, "g": "GLOBAL"},
        headers=headers,
        allow_redirects=False)
    get_data = get_req.json().get('data').get('children')
    if get_req.status_code == 200:
        for posts in get_data:
            print(posts.get('data').get('title'))
    else:
        print("None")
