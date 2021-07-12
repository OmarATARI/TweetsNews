"""Database engine & session creation."""
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from models import Base
import time

flag = True
while flag:
  try:
    engine = create_engine(
        'postgresql://user:pwd@postgres:5432/tweets',
        echo=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    flag = False
  except exc.OperationalError:
    print('Waiting for database...')
    time.sleep(1)
  else:
    break