#!/usr/bin/python3
"""Get top ten hot posts"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agen': 'top_ten_posts/1.0'}
    res = requests.get(url, headers=header, allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        posts = data.get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print(None)
