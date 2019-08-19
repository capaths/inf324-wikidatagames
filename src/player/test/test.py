""" Service unit testing best practice, with an alternative dependency.
"""

import pytest
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


def test_service(session):

    # create instance, providing the test database session
    service = worker_factory(PlayerService, db=session)

    # verify ``save`` logic by querying the test database
    service.save("helloworld")
    assert session.query(Result.value).all() == [("helloworld",)]

