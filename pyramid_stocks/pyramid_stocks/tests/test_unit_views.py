def test_default_response_portfolio_view(dummy_request):
    from ..views.portfolio import portfolio_view

    response = portfolio_view(dummy_request)
    assert isinstance(response, dict)
    assert response['data'] == []


# def test_default_detail_view(dummy_request, db_session, test_entry):
#     from ..views.portfolio import detail_view

#     db_session.add(test_entry)

#     dummy_request.matchdict = {'symbol': 'fake'}
#     response = detail_view(dummy_request)
#     assert response['data'].symbol == 'fake'


def test_detail_not_found(dummy_request):
    from ..views.portfolio import detail_view
    from pyramid.httpexceptions import HTTPNotFound

    response = detail_view(dummy_request)
    assert isinstance(response, HTTPNotFound)

def test_default_response_new_view(dummy_request):
    from ..views.portfolio import add_view

    response = add_view(dummy_request)
    assert len(response) == 0
    assert type(response) == dict


def test_valid_post_to_new_view(dummy_request):
    from ..views.portfolio import add_view
    from pyramid.httpexceptions import HTTPFound

    dummy_request.method = 'POST'
    dummy_request.POST = {
        'symbol': 'fake',
        'companyName': 'some fake body of information',
        'industry': 'the best one',
        'website': 'brandon@brandon.brandon',
        'sector': '9',
        'CEO': 'Brandon Brandon',
        'issueType': 'top secret',
        'exchange': 'usofa',
        'description': '01-01-2018',
    }

    response = add_view(dummy_request)
    assert response.status_code == 302
    assert isinstance(response, HTTPFound)


def test_valid_post_to_new_view_adds_record_to_db(dummy_request, db_session):
    from ..views.portfolio import add_view
    from ..models import Stock

    dummy_request.method = 'POST'
    dummy_request.POST = {
        'symbol': 'fake',
        'companyName': 'fake',
        'industry': 'the best one',
        'website': 'brandon@brandon.brandon',
        'sector': '9',
        'CEO': 'Brandon Brandon',
        'issueType': 'top secret',
        'exchange': 'usofa',
        'description': '01-01-2018',
    }

    # assert right here that there's nothing in the DB

    add_view(dummy_request)
    query = db_session.query(Stock)
    one = query.first()
    assert one.symbol == 'fake'
    assert one.companyName == 'fake'
    assert type(one.symbol) == str


def test_invalid_post_to_new_view(dummy_request):
    import pytest
    from ..views.portfolio import add_view
    from pyramid.httpexceptions import HTTPBadRequest

    dummy_request.method = 'POST'
    dummy_request.POST = {}

    with pytest.raises(HTTPBadRequest):
        response = add_view(dummy_request)
        assert isinstance(response, HTTPBadRequest)
