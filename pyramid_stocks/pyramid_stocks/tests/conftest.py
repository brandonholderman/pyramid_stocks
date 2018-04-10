import pytest
from pyramid import testing

@pytest.fixture
def dummy_request():
    return testing.DummyRequest()

@pytest.fixture
def create_new_entry():
    pass

@pytest.fixture
def configuration(request):
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://localhost:5432/entries_test'
    })

    config.include('pyramid_stocks.models')
    config.include('pyramid_stocks.routes')

    def teardown():
        testing.tearDown()

    request.addfinalizers(teardown)
    return config

@pytest.fixture
def db_session(configuration, request):
    SessionFactory = configuration.registry['dbsession_factory']
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        base.metadata.drop_all(engine)

    request.addfinalizers(teardown)
    return session

@pytest.fixture
def dummy_request(db_session):
    pass