#!/usr/bin/python3
"""Get list of titles recursevly"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'recurse_all_posts/1.0'}
    payload = {'limit': 200, 'after': after}
    res = requests.get(
            url, headers=header, params=payload, allow_redirects=False)

    if res.status_code == 200:
        json = res.json()
        data = json.get('data')
        posts = data.get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))

        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list
    else:
        return None
