#!/usr/bin/env python3

import requests
from urllib.parse import unquote
from database import session
from models import Tweet
import os, time, logging

def get_tweets(q, lang, cpt = 1):
    auth_token = os.environ['TWITTER_BEARER']
    hed = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get('https://api.twitter.com/1.1/search/tweets.json?q={0}&lang={1}'.format(q, lang), headers=hed)
    try:
        data = response.json()['statuses'] 

        results = []
        for d in data:
            current_tweet = Tweet(
                tweet=unquote(d['text']),
                created_at=d['created_at'],
                tweet_id=d['id_str'],
                language=d['lang'],
                author=d['user']['name']
                )
            session.add(current_tweet)

        session.commit()
        return results
    except requests.exceptions.Timeout:
        if cpt <= 3:
            time.sleep(3)
            get_tweets(q, lang, cpt = cpt+1)
        else:
            logging.error('TimeOut: Max retry excedded for the api call')
    except requests.exceptions.TooManyRedirects:
        logging.error('TooManyRedirects: Check the URL')
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occured when you called the twitter api: {e}")


def get_tweets_by_city(q, lang, geocode, city, cpt = 1):
    auth_token = os.environ['TWITTER_BEARER']
    hed = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get('https://api.twitter.com/1.1/search/tweets.json?q={0}&lang={1}&geocode={2}'.format(q, lang, geocode), headers=hed)
    try:
        data = response.json()['statuses'] 

        results = []
        for d in data:
            current_tweet = Tweet(
                tweet=unquote(d['text']),
                created_at=d['created_at'],
                tweet_id=d['id_str'],
                language=d['lang'],
                author=d['user']['name'],
                geocode=geocode,
                city=city
                )
            session.add(current_tweet)

        session.commit()
        return results
    except requests.exceptions.Timeout:
        if cpt <= 3:
            time.sleep(3)
            get_tweets(q, lang, cpt = cpt+1)
        else:
            logging.error('TimeOut: Max retry excedded for the api call')
    except requests.exceptions.TooManyRedirects:
        logging.error('TooManyRedirects: Check the URL')
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occured when you called the twitter api: {e}")

def get_tweets_paris(q, lang):
    return get_tweets_by_city(q, lang, '48.8566969,2.3514616,10km', 'Paris')

def get_tweets_ny(q, lang):
    return get_tweets_by_city(q, lang, '40.7127281,-74.0060152,10km', 'New-York')

def get_tweets_london(q, lang):
    return get_tweets_by_city(q, lang, '51.5073219,-0.1276474,10km', 'Londres')

def get_tweets_tokyo(q, lang):
    return get_tweets_by_city(q, lang, '35.6828387,139.7594549,10km', 'Tokyo')

def get_tweets_sydney(q, lang):
    return get_tweets_by_city(q, lang, '-33.8548157,151.2164539,10km', 'Sydney')

def get_tweets_seoul(q, lang):
    return get_tweets_by_city(q, lang, '37.5666791,126.9782914,10km', 'Seoul')