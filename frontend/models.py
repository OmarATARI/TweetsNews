from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, Float, DateTime, BigInteger

Base = declarative_base()

class Tweet(Base):
  """Tweet"""

  __tablename__ = "tweets"
  id = Column(BigInteger, primary_key=True, autoincrement="auto")
  tweet = Column(String)
  created_at = Column(DateTime)
  tweet_id = Column(String)
  language = Column(String)
  author = Column(String)

  def __repr__(self):
    return "<Tweet %r>" % self.tweet_id

  def serialize(self):
    return {
      'id': self.id,
      'tweet': self.tweet,
      'created_at': self.created_at,
      'tweet_id': self.tweet_id,
      'language': self.language,
      'author': self.author
    }

class Trend(Base):
  """"TweetsTrend"""

  __tablename__ = "trends"
  id = Column(BigInteger, primary_key=True, autoincrement="auto")
  title = Column(String)
  url = Column(String)
  location_city = Column(String)
  woeid = Column(Integer)

  def __repr__(self):
    return "<Trend %r>" % self.name

  def serialize(self):
    return {
      'id': self.id,
      'title': self.title,
      'url': self.url,
      'location_city': self.location_city,
      'woeid': self.woeid
    }