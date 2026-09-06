from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os


load_dotenv() #Carga las variables de .env


DATABASE_URL = os.getenv('DATABASE_URL')


if not DATABASE_URL:
    raise RuntimeError('BD npt found ')

engine = create_engine(DATABASE_URL)

'''
SessionLocal no es una Session.
Es una fábrica de Sessions.
'''
session = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass