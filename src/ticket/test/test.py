import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from nameko.testing.services import worker_factory
from ticket.service import TicketService
from ticket.models import DeclarativeBase, Ticket, TicketRepository

import json

TEST_TITLE = "Test Ticket"
TEST_CONTENT = "This is a ticket content"


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    DeclarativeBase.metadata.create_all(engine)

    session_cls = sessionmaker(bind=engine)
    rep = TicketRepository(session_cls())

    return rep


def test_create(session):
    service = worker_factory(TicketService, rep=session)
    assert service.create_ticket(TEST_TITLE, TEST_CONTENT)


def test_get_tickets(session):
    service = worker_factory(TicketService, rep=session)

    assert len(service.get_all_tickets()) == 0
    session.db.add(Ticket(title=TEST_TITLE, content=TEST_CONTENT))
    session.db.add(Ticket(title=TEST_TITLE, content=TEST_CONTENT))
    session.db.commit()
    assert len(service.get_all_tickets()) == 2
    assert service.get_all_tickets()[0]["title"] == TEST_TITLE
    assert service.get_all_tickets()[0]["content"] == TEST_CONTENT
