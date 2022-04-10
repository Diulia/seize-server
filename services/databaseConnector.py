from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 

password = os.environ['DB_PASSWORD']
address = os.environ['DB_ADDRESS']
port = os.environ['DB_PORT']

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{password}@{address}:{port}/seize"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo='debug'
)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
