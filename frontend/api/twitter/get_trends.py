#!/usr/bin/env python3

import requests
from urllib.parse import unquote

def main_endpoint(woeid):
    auth_token='AAAAAAAAAAAAAAAAAAAAACAROAEAAAAALeao4ZMCbqGOfsvgdWg7en0wWsI%3DbVUSaFnSGBqKBwX9kqYmTsCypNOfx6MoutaVEyZEgvBmsW1W7z'
    hed = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get("https://api.twitter.com/1.1/trends/place.json?id={0}".format(woeid), headers=hed)
    data = response.json()[0]['trends']

    results = []
    for d in data:
      results.append([unquote(d['query']), d['url']])

    return results

def get_paris_trends():
    return main_endpoint(615702)

def get_london_trends():
    return main_endpoint(44418)

def get_ny_trends():
    return main_endpoint(2459115)

def get_tokyo_trends():
    return main_endpoint(1118370)

def get_sydney_trends():
    return main_endpoint(1105779)

def get_seoul_trends():
    return main_endpoint(1132599)
