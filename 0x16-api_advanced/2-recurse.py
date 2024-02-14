#!/usr/bin/python3
"""Get list of titles recursevly"""
import requests
import time


def helper(url, hot_list, after):
    header = {'User-Agen': 'recurse_all_posts/1.0'}
    payload = {'limit': 5, 'count': len(hot_list), 'after': after}
    res = requests.get(url, headers=header,
                       params=payload, allow_redirects=False)

    if res.status_code == 429:
        time.sleep(5)
        helper(url, hot_list, after)

    json = res.json()
    data = json.get('data')

    if not data or not data.get('before'):
        return 0

    if res.status_code == 200:
        posts = data.get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))

        helper(url, hot_list, data.get('after'))


def recurse(subreddit, hot_list=[]):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agen': 'recurse_all_posts/1.0'}
    res = requests.get(url, headers=header,
                       params={'limit': 5}, allow_redirects=False)

    if res.status_code == 429:
        time.sleep(5)
        recurse(subreddit)

    json = res.json()
    data = json.get('data')

    if res.status_code == 200:
        posts = data.get('children')
        for post in posts[1:]:
            hot_list.append(post.get('data').get('title'))
        helper(url, hot_list, data.get('after'))
        return hot_list
    else:
        None
