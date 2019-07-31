from sqlalchemy import (
    DECIMAL, Column, DateTime, ForeignKey, Integer,String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker






class Player(DeclarativeBase):
    __tablename__ = "Player"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(50))
    country = Column(String(50))
    elo = Column(Integer)

DeclarativeBase = declarative_base(name=players)