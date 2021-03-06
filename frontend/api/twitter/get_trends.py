#!/usr/bin/env python3

import requests
from urllib.parse import unquote
from database import session
from models import Trend
import os

def main_endpoint(woeid, city_title):
    auth_token = os.environ['TWITTER_BEARER']
    hed = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get("https://api.twitter.com/1.1/trends/place.json?id={0}".format(woeid), headers=hed)
    if response.status_code == 200:
        data = response.json()[0]['trends']

        results = []
        for d in data:
            current_trend = Trend(title=unquote(d['query']), url=d['url'], woeid=woeid, location_city=city_title)
            session.add(current_trend)
            results.append([unquote(d['query']), d['url']])

        session.commit()
        return results
    else:
        print('An Error occured')
        return False

def get_paris_trends():
    return main_endpoint(615702, 'Paris')

def get_london_trends():
    return main_endpoint(44418, 'London')

def get_ny_trends():
    return main_endpoint(2459115, 'New-York')

def get_tokyo_trends():
    return main_endpoint(1118370, 'Tokyo')

def get_sydney_trends():
    return main_endpoint(1105779, 'Syndey')

def get_seoul_trends():
    return main_endpoint(1132599, 'Seoul')
