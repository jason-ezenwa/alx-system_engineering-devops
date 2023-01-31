#!/usr/bin/python3
""" returns the number of subscribers for a subreddit"""
import requests


def top_ten(subreddit):
    headers = {"User-Agent": "CustomUser"}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    jsonresp = response.json()
    posts = jsonresp['data']['children']
    for post in posts:
        print(post['data']['title'])

