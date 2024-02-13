#!/usr/bin/python3
"Get subs count for a subreddit"
import requests


def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    payload = {'q': subreddit}
    res = requests.get(url,  params=payload)
    data = res.json()
    if res.status_code == 200:
        return data.get('data').get('subscribers')
    
    return 0
    