from sqlalchemy import (
    Column, DateTime, Integer, String, UnicodeText
)

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

import datetime


def get_url():
    return (
        "postgresql://{db_user}:{db_pass}@{db_host}:"
        "{db_port}/{db_name}"
    ).format(
        db_user=os.getenv("DB_USER", "postgres"),
        db_pass=os.getenv("DB_PASSWORD", "password"),
        db_host=os.getenv("DB_HOST", "localhost"),
        db_port=os.getenv("DB_PORT", "5432"),
        db_name=os.getenv("DB_NAME", "ticket"),
    )


engine = create_engine(get_url())
DeclarativeBase = declarative_base()


class Ticket(DeclarativeBase):
    __tablename__ = "Ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(UnicodeText)
    date_sent = Column(DateTime, default=datetime.datetime.utcnow)


DeclarativeBase.metadata.create_all(engine)
