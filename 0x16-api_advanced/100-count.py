#!/usr/bin/python3
"""Count number of appearences recursevly"""
import requests

words_count = {}


def count_words(subreddit, word_list, after=None):
    global words_count
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    header = {'User-Agent': 'count_word/1.0'}
    payload = {'limit': 200, 'after': after}
    res = requests.get(
            url, headers=header, params=payload, allow_redirects=False)

    if res.status_code != 200:
        return

    data = res.json().get('data')
    posts = data.get('children')
    for post in posts:
        title = post.get('data').get('title').lower()
        words = title.split()
        for word in words:
            if word in word_list:
                words_count[word] = words_count.get(word, 0) + 1

    after = data.get('after')
    if not after:
        sorted_count = sorted(words_count.items(), key=lambda e: (-e[1], e[0]))
        for k, v in sorted_count:
            print(f'{k}: {v}')
    else:
        count_words(subreddit, word_list, after)
