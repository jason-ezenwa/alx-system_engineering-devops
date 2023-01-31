#!usr/bin/python3
""" returns the number of subscribers for a subreddit"""
import requests


def number_of_subscribers(subreddit):
    headers = {"User-Agent": "CustomUser"}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    jsonresp = response.json()
    return (jsonresp['data']['subscribers'])
