import pytest
from pyramid import testing
from ..models.meta import Base
from ..models import Stock
import os

@pytest.fixture
def test_entry():
    return Stock(
        symbol='fake',
        companyName='some fake body of information',
        industry='the best one',
        website='brandon@brandon.brandon',
        sector='9',
        CEO='Brandon Brandon',
        issueType='top secret',
        exchange='usofa',
        description='01-01-2018',
    )

@pytest.fixture
def configuration(request):
    config = testing.setUp(settings={
        'sqlalchemy.url': os.environ.get('TEST_DATABASE_URL')
    })

    config.include('pyramid_stocks.models')
    config.include('pyramid_stocks.routes')

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config

@pytest.fixture
def db_session(configuration, request):
    SessionFactory = configuration.registry['dbsession_factory']
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session

@pytest.fixture
def dummy_request(db_session):
    """Create a dummy GET request with a dbsession."""
    return testing.DummyRequest(dbsession=db_session)
