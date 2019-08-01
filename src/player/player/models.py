from sqlalchemy import (
    DECIMAL, Column, DateTime, ForeignKey, Integer,String
)

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

def get_url():
    return (
        "postgresql://{db_user}:{db_pass}@{db_host}:"
        "{db_port}/{db_name}"
    ).format(
        db_user=os.getenv("DB_USER", "postgres"),
        db_pass=os.getenv("DB_PASSWORD", "password"),
        db_host=os.getenv("DB_HOST", "localhost"),
        db_port=os.getenv("DB_PORT", "5432"),
        db_name=os.getenv("DB_NAME", "orders"),
    )


engine = create_engine(get_url())
DeclarativeBase = declarative_base()


class Player(DeclarativeBase):
    __tablename__ = "Player"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(50))
    country = Column(String(50))
    elo = Column(Integer)


DeclarativeBase.metadata.create_all(engine)
