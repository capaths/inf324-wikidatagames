import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from nameko.testing.services import worker_factory
from player.service import PlayerService
from player.models import DeclarativeBase, Player, PlayerRepository

TEST_USERNAME = "TestUser"
TEST_USERNAME2 = "TestUser2"
TEST_PASSWORD = "secret"


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    DeclarativeBase.metadata.create_all(engine)

    session_cls = sessionmaker(bind=engine)
    rep = PlayerRepository(session_cls())

    test_player = Player(username=TEST_USERNAME, password=TEST_PASSWORD, country="Chile")
    rep.db.add(test_player)

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
    assert service.get_player(TEST_USERNAME, TEST_PASSWORD) is not None


def test_get_player_by_username(session):
    service = worker_factory(PlayerService, rep=session)
    assert service.get_player_by_username(TEST_USERNAME) is not None
