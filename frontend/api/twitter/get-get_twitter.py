
import requests
from urllib.parse import unquote
from database import session
from sqlalchemy.sql.sqltypes import Date
from models import Tweet


def main_endpoint(q,lang):
    auth_token = 'AAAAAAAAAAAAAAAAAAAAACAROAEAAAAALeao4ZMCbqGOfsvgdWg7en0wWsI%3DbVUSaFnSGBqKBwX9kqYmTsCypNOfx6MoutaVEyZEgvBmsW1W7z'
    hed = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get("https://api.twitter.com/1.1/search/tweets.json?q={0}&lang={1}".format(q,lang), headers=hed)
    data = response.json()['statuses']
    #Date, Tweet, Langue =  [],  [],  []  
    results = []
    for d in data:
        #Date.append(d['created_at'])
        #Tweet.append(d['text'])
        #Langue.append(d['lang'])
    #print(Date)
    #print(Tweet)
    #print(Langue)
    #return Date,Tweet,Langue
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

main_endpoint()



