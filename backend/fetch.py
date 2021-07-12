#!/usr/bin/env python3

import requests

# Quick start - code sample with covid subject
auth_token='AAAAAAAAAAAAAAAAAAAAACAROAEAAAAALeao4ZMCbqGOfsvgdWg7en0wWsI%3DbVUSaFnSGBqKBwX9kqYmTsCypNOfx6MoutaVEyZEgvBmsW1W7z'
hed = {'Authorization': 'Bearer ' + auth_token}
response = requests.get("https://api.twitter.com/2/tweets/search/recent?tweet.fields=lang&media.fields=&query=covid", headers=hed)
data = response.json()['data']
for d in data:
    print(f"ID: {d['id']}")
    print(f"Langue: {d['lang']}")
    print(f"Contenu: {d['text']}")
