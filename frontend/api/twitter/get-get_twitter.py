
import requests
from urllib.parse import unquote

from sqlalchemy.sql.sqltypes import Date


def main_endpoint():
    auth_token = 'AAAAAAAAAAAAAAAAAAAAACAROAEAAAAALeao4ZMCbqGOfsvgdWg7en0wWsI%3DbVUSaFnSGBqKBwX9kqYmTsCypNOfx6MoutaVEyZEgvBmsW1W7z'
    hed = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get("https://api.twitter.com/1.1/search/tweets.json?q=covid&lang=fr".format(), headers=hed)
    data = response.json()['statuses']
    Date, Tweet, Langue =  [],  [],  []  
    for d in data:
        Date.append(d['created_at'])
        Tweet.append(d['text'])
        Langue.append(d['lang'])
    print(Date)
    print(Tweet)
    print(Langue)
    return Date,Tweet,Langue

main_endpoint()



