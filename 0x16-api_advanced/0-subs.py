#!/usr/bin/python3
""" Queries the Reddit API and returns the number
    of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ Query for a reddit subscribers """
    headers = {'User-agent': 'monicajoa'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    get_sudreddit = requests.get(url, headers=headers, allow_redirects=False)
    if get_sudreddit.status_code == 200:
        subs_query = get_sudreddit.json().get('data').get('subscribers')
        return subs_query
    else:
        return 0
