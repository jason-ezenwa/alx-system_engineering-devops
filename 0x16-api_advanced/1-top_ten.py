#!usr/bin/python3
""" returns the number of subscribers for a subreddit"""
import requests


def top_ten(subreddit):
    headers = {"User-Agent": "CustomUser"}
    url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    jsonresp = response.json()
    posts = jsonresp['data']['children']
    for post in range(0, 10):
        print(posts[post]['data']['title'])

