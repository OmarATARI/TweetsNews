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
  tweet_id = Column(String)
  language = Column(String)

  def __repr__(self):
    return "<Tweet %r>" % self.name

  def serialize(self):
    return {
      'id': self.id,
      'tweet': self.tweet,
      'tweet_id': self.tweet_id,
      'language': self.language
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