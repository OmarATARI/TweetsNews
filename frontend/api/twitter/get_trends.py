#!/usr/bin/env python3

import requests
from urllib.parse import unquote
from database import session
from models import Trend
import os
import time
import logging

def main_endpoint(woeid, city_title, cpt = 1):
    auth_token = os.environ['TWITTER_BEARER']
    hed = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get("https://api.twitter.com/1.1/trends/place.json?id={0}".format(woeid), headers=hed)
    try:
        data = response.json()[0]['trends']

        results = []
        for d in data:
            current_trend = Trend(title=unquote(d['query']), url=d['url'], woeid=woeid, location_city=city_title)
            session.add(current_trend)
            results.append([unquote(d['query']), d['url']])

        session.commit()
        return results
    except requests.exceptions.Timeout:
        if cpt <= 3:
            time.sleep(3)
            main_endpoint(woeid, city_title, cpt= cpt+1)
        else:
            logging.error('TimeOut: Max retry excedded for the api call')
    except requests.exceptions.TooManyRedirects:
        logging.error('TooManyRedirects: Check the URL')
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occured when you called the twitter api: {e}")

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
