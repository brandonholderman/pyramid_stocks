# import unittest
# import transaction

# from pyramid import testing


# def dummy_request(dbsession):
#     return testing.DummyRequest(dbsession=dbsession)


# class BaseTest(unittest.TestCase):
#     def setUp(self):
#         self.config = testing.setUp(settings={
#             'sqlalchemy.url': 'sqlite:///:memory:'
#         })
#         self.config.include('.models')
#         settings = self.config.get_settings()

#         from .models import (
#             get_engine,
#             get_session_factory,
#             get_tm_session,
#             )

#         self.engine = get_engine(settings)
#         session_factory = get_session_factory(self.engine)

#         self.session = get_tm_session(session_factory, transaction.manager)

#     def init_database(self):
#         from .models.meta import Base
#         Base.metadata.create_all(self.engine)

#     def tearDown(self):
#         from .models.meta import Base

#         testing.tearDown()
#         transaction.abort()
#         Base.metadata.drop_all(self.engine)


# class TestMyViewSuccessCondition(BaseTest):

#     def setUp(self):
#         super(TestMyViewSuccessCondition, self).setUp()
#         self.init_database()

#         from .models import MyModel

#         model = MyModel(name='one', value=55)
#         self.session.add(model)

#     def test_passing_view(self):
#         from .views.default import my_view
#         info = my_view(dummy_request(self.session))
#         self.assertEqual(info['one'].name, 'one')
#         self.assertEqual(info['project'], 'pyramid_stocks')


# class TestMyViewFailureCondition(BaseTest):

#     def test_failing_view(self):
#         from .views.default import my_view
#         info = my_view(dummy_request(self.session))
#         self.assertEqual(info.status_int, 500)

def test_default_behavior_of_base_route(dummy_request):
    from ..views.default import index_view
    from pyramid.response import Response

    request = dummy_request
    response = index_view(request)
    assert isinstance(response, Response)
    assert response.text == 'I did a thing'


def test_default_behavior_of_entries_views(dummy_request):
    from ..views.default import entries.view

    response = entries_view(dummy_request)
    assert type(response) == dict
