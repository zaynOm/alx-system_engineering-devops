#!/usr/bin/python3
"Get subs count for a subreddit"
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agen': 'number_of_subs/1.0'}
    res = requests.get(url)
    data = res.json()
    
    if res.status_code == 200:
        return data.get('data').get('subscribers')

    return 0
