from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = (
    "postgresql+psycopg://"
    "enrique:2540712"
    "@localhost:5433/expense_manager"
)

engine = create_engine(DATABASE_URL)

'''
SessionLocal no es una Session.
Es una fábrica de Sessions.
'''
session = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass