#!/usr/bin/env python3

import requests
from urllib.parse import unquote
from database import session
from models import Tweet

def get_tweets(q, lang):
    auth_token = 'AAAAAAAAAAAAAAAAAAAAACAROAEAAAAALeao4ZMCbqGOfsvgdWg7en0wWsI%3DbVUSaFnSGBqKBwX9kqYmTsCypNOfx6MoutaVEyZEgvBmsW1W7z'
    hed = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get('https://api.twitter.com/1.1/search/tweets.json?q={0}&lang={1}'.format(q, lang), headers=hed)
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


## Réponse type de l'api - data variable

# {'created_at': 'Fri Jul 16 08:29:54 +0000 2021', 
# 'id': 1415951814562885637, 
# 'id_str': '1415951814562885637', 
# 'text': "RT @AKMEMETEAU: Délai entre la découverte d'un vaccin et l'obligation vaccinale : \n- BCG : 1921 obligatoire en 1950\n- Diphtérie : 1923 obli…", 
# 'truncated': False, 
# 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'AKMEMETEAU', 'name': 'Philippe_Mèmeteau', 'id': 1244985114829959173, 'id_str': '1244985114829959173', 
# 'indices': [3, 14]}], 
# 'urls': []}, 
# 'metadata': {'iso_language_code': 'fr', 'result_type': 'recent'}, 
# 'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', 
# 'in_reply_to_status_id': None, 
# 'in_reply_to_status_id_str': None, 
# 'in_reply_to_user_id': None, 
# 'in_reply_to_user_id_str': None, 
# 'in_reply_to_screen_name': None, 
# 'user': {'id': 1387664851489759233, 'id_str': '1387664851489759233', 'name': 'Mickey', 'screen_name': 'Mickey86164385', 'location': '', 'description': '', 'url': None, 'entities': {'description': {'urls': []}},
# 'protected': False, 
# 'followers_count': 49, 
# 'friends_count': 173, 
# 'listed_count': 0, 
# 'created_at': 'Thu Apr 29 07:08:22 +0000 2021', 
# 'favourites_count': 1758, 'utc_offset': None, 
# 'time_zone': None, 'geo_enabled': False, 
# 'verified': False, 'statuses_count': 1111, 
# 'lang': None, 
# 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png', 'profile_image_url_https': 'https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': True, 'following': None, 'follow_request_sent': None, 'notifications': None, 'translator_type': 'none', 'withheld_in_countries': []}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'retweeted_status': {'created_at': 'Fri Jul 16 07:14:23 +0000 2021', 'id': 1415932809177411584, 'id_str': '1415932809177411584', 'text': "Délai entre la découverte d'un vaccin et l'obligation vaccinale : \n- BCG : 1921 obligatoire en 1950\n- Diphtérie : 1… https://t.co/B4TMtQxO0o", 'truncated': True, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/B4TMtQxO0o', 'expanded_url': 'https://twitter.com/i/web/status/1415932809177411584', 'display_url': 'twitter.com/i/web/status/1…', 'indices': [117, 140]}]}, 'metadata': {'iso_language_code': 'fr', 'result_type': 'recent'}, 'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 1244985114829959173, 'id_str': '1244985114829959173', 'name': 'Philippe_Mèmeteau', 'screen_name': 'AKMEMETEAU', 'location': 'La Rochelle', 'description': "Dirigeant de l'agence AKtiv design - Graphisme Multimédia/Web/Photo/Vidéo/Drone/ La seule agence de Com' installée sur un bateau historique à La Rochelle.", 'url': 'https://t.co/gOamltblNE', 'entities': {'url': {'urls': [{'url': 'https://t.co/gOamltblNE', 'expanded_url': 'https://www.aktivdesign.net', 'display_url': 'aktivdesign.net', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 4341, 'friends_count': 2610, 'listed_count': 10, 'created_at': 'Tue Mar 31 13:49:30 +0000 2020', 'favourites_count': 2398, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 2497, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1244985379360555008/34vTuHrX_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1244985379360555008/34vTuHrX_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1244985114829959173/1585664273', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None, 'translator_type': 'none', 'withheld_in_countries': []}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 160, 'favorite_count': 187, 'favorited': False, 'retweeted': False, 'lang': 'fr'}, 
# 'is_quote_status': False, 'retweet_count': 160, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'fr'}
