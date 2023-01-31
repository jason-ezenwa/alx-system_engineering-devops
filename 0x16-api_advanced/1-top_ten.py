#!/usr/bin/python3
""" returns the number of subscribers for a subreddit"""
import requests


def top_ten(subreddit):
    try:
        headers = {"User-Agent": "CustomUser"}
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        response = requests.get(url, headers=headers, allow_redirects=False)
        jsonresp = response.json()
        posts = jsonresp['data']['children']
        for post in range(0, 10):
            print(posts[post]['data']['title'])
    except KeyError:
        print(None)

