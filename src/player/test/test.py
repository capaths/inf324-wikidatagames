""" Service unit testing best practice, with an alternative dependency.
"""

import pytest, json
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from nameko.rpc import rpc
from nameko.testing.services import worker_factory
from player.service import *
from player.models import *

@pytest.fixture
def session():
    """ Create a test database and session
    """
    #Base.metadata.create_all(engine)

    engine = create_engine('sqlite:///:memory:')
    DeclarativeBase.metadata.create_all(engine)

    session_cls = sessionmaker(bind=engine)
    return PlayerRepository(session_cls())

"""
def test_create(session):

    # create instance, providing the test database session
    service = worker_factory(PlayerService, rep=session)

    # verify ``save`` logic by querying the test database

    testDict = {
        'username': 'test',
        'password': 'test123',
        'country': 'Testland',
        'elo': 10
    }
    testJson = json.dumps(testDict)

    testDict2 = {
        'username': 'test',
        'password': 'test123',
        'country': 'Testland',
        'elo': 10
    }
    testJson2 = json.dumps(testDict2)


    assert service.create_player(testJson)
    assert service.create_player(testJson2)
"""


def test_get_player(session):
    service = worker_factory(PlayerService, rep=session)
    username = "testest"
    password = "testest"
    assert service.get_player(username, password)


def test_get_player_by_username(session):
    service = worker_factory(PlayerService, rep=session)
    username = "testest"
    assert service.get_player_by_username(username) is None