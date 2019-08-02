from sqlalchemy import (
    DECIMAL, Column, DateTime, ForeignKey, Integer,String, LargeBinary
)


import os
from sqlalchemy import UniqueConstraint
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


class Ticket(DeclarativeBase):
    __tablename__ = "Ticket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    description = Column(String(50))


DeclarativeBase.metadata.create_all(engine)