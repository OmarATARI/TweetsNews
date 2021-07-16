from flask import (Flask, Response, request, jsonify, render_template)
from datetime import datetime

from api.twitter.get_trends import *
from api.twitter.get_tweets import get_tweets
from forms import ExportForm
from models import Tweet
from io import StringIO
import csv

# from forms import ExportForm

from flask import Flask, render_template
from forms import ExportForm, SearchTweetsForm

app = Flask(__name__)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pwd@localhost/tweets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404

@app.route('/search_tweets')
def search_tweets():
    """Search tweets form"""
    form = SearchTweetsForm()
    return render_template('Lasttweet/search.html', form=form)

@app.route('/search_api')
def search_api():
    """Fetch tweets from api"""
    form = SearchTweetsForm()
    get_tweets(request.args.get('term'), request.args.get('lang'))
    searched_tweets = session.query(Tweet).filter(
        Tweet.tweet.contains(request.args.get('term')),
        Tweet.language == request.args.get('lang')
    )
    
    return render_template('Lasttweet/search.html', form=form, tweets=searched_tweets)


@app.route('/last_tweet')
def last_tweet():
    """Trend Last Tweet"""
    # peuple la base avec une recherche simple sur le covid en français
    get_tweets('covid', 'fr')
    # récupération des tweets à partir de la base de données
    all_tweets = session.query(Tweet).all()

    return render_template('Lasttweet/accueil.html', tweets=all_tweets)

@app.route('/last_trend/paris')
def paris_trend():
    """Trend Last Tweet"""
    trends_by_location = {
        'Paris': get_paris_trends()
    }
    return render_template('LastTrend/City/Paris.html', trends=trends_by_location)

@app.route('/last_trend/london')
def london_trend():
    """Trend Last Tweet"""
    trends_by_location = {
        'Londres': get_london_trends()
    }
    return render_template('LastTrend/City/London.html', trends=trends_by_location)

@app.route('/last_trend/newyork')
def newyork_trend():
    """Trend Last Tweet"""
    trends_by_location = {
        'New-York': get_ny_trends()

    }
    return render_template('LastTrend/City/NewYork.html', trends=trends_by_location)

@app.route('/last_trend/seoul')
def seoul_trend():
    """Trend Last Tweet"""
    trends_by_location = {
        'Seoul': get_seoul_trends()
    }
    return render_template('LastTrend/City/Seoul.html', trends=trends_by_location)

@app.route('/last_trend/sydney')
def sydney_trend():
    """Trend Last Tweet"""
    trends_by_location = {
        'Syndey': get_sydney_trends()
    }
    return render_template('LastTrend/City/Sydney.html', trends=trends_by_location)


@app.route('/last_trend/tokyo')
def tokyo_trend():
    """Trend Last Tweet"""
    trends_by_location = {
        'Tokyo': get_tokyo_trends()

    }
    return render_template('LastTrend/City/Tokyo.html', trends=trends_by_location)


@app.route('/last_trend')
def last_trend():
    """Trend Last Tweet"""
    trends_by_location = {
        'Paris': get_paris_trends(),
        'Londres': get_london_trends(),
        'New-York': get_ny_trends(),
        'Tokyo': get_tokyo_trends(),
        'Syndey': get_sydney_trends(),
        'Seoul': get_seoul_trends()
    }
    return render_template('LastTrend/accueil.html', trends=trends_by_location)


@app.route('/export_tweet')
def export_tweet():
    """Trend Last Tweet"""
    form = ExportForm()
    return render_template('Export/accueil.html', form=form)

def parse_datetime(str_date) -> datetime:
  """
    Parse a datetime string with the format %Y-%m-%d %H:%M:%S

    Parameters
    ----------
    str_date : str
      the datetime

    Returns
    -------
    datetime
  """
  return datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')

@app.route('/search')
def search():
  output = StringIO()
  cw = csv.DictWriter(output,
    fieldnames=['id', 'tweet', 'created_at', 'tweet_id', 'language', 'author'])
  cw.writeheader()

  author = request.args.get('author')
  term = request.args.get('term')
  start_datetime = parse_datetime(request.args.get('day_start')+ ' ' + request.args.get('hour_start'))
  end_datetime = parse_datetime(request.args.get('day_end')+ ' ' + request.args.get('hour_end'))
  tweets = session.query(Tweet).filter(
      Tweet.author.contains(author),
      Tweet.tweet.contains(term),
      Tweet.created_at <= end_datetime, 
      Tweet.created_at >= start_datetime)
  data = [t.serialize() for t in tweets]

  for d in data:
    cw.writerow(d)

  return Response(output.getvalue(), mimetype="text/csv")

# @app.route('/export')
# def export():
#   form = ExportForm()
#   return render_template('export.html', form=form)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
