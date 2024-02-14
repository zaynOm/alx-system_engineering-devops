#!/usr/bin/python3
"""Get subs count for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Number of subs"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agen': 'number_of_subs/1.0'}
    res = requests.get(url, headers=header, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        return data.get('data').get('subscribers')

    return 0
