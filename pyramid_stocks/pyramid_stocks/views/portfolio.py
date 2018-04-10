from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError
from ..models import Stock
from . import DB_ERROR_MSG
import requests
import json
import os

API_URL = 'https://api.iextrading.com/1.0'
API_KEY = os.environ.get('API_KEY', '')

@view_config(
    route_name='portfolio',
    renderer='../templates/portfolio.jinja2',
    request_method='GET')
def portfolio_view(request):
    """
    Directs user to their portfolio template
    """
    try:
        query = request.dbsession.query(Stock)
        all_entries = query.all()
    except DBAPIError:
        return DBAPIError(DB_ERROR_MSG, content_type='text/plain', status=500)

    return {'data': all_entries}


@view_config(
    route_name='detail',
    renderer='../templates/detail.jinja2',
    request_method='GET')
def detail_view(request):
    """
    Directs user to the detail template
    """
    try:
        symbol = request.matchdict['symbol']
    except KeyError:
        return HTTPNotFound()

    try:
        query = request.dbsession(Stock)
        stock_detail = query.filter(Stock.symbol == symbol).first()
    except DBAPIError:
        return Response(DB_ERROR_MSG, content_type='text/plain', status=500)

    res = request.get('https://pixabay.com/api?key={}&q={}'.format(API_KEY, stock_detail.title.split(' ')[0]))

    try:
        url=res.json()['hits'][0]['webformatURL']
    except (KeyError, IndexError):
        url='https://via.placeholder.com/300x300'
    return {
        "entry": stock_detail,
        "img": url,
    }

        # for data in API_URL:
        #     if data['symbol'] == symbol:
        #         return {'data': data}
        # return {}

@view_config(
    route_name='add',
    renderer='../templates/add.jinja2',
    request_method='GET')
def add_view(request):
    """
    Directs user to the add stock template
    """
    if request.method == 'POST':
        if not all([field in request.POST for field in ['title', 'body', 'date', 'author']]):
            raise HTTPBadRequest

        instance = Stock(
            id=request.POST['id'],
            symbol=request.POST['symbol'],
            companyName=request.POST['companyName'],
            website=request.POST['website'],
            industry=request.POST['industry'],
            sector=request.POST['sector'],
            CEO=request.POST['CEO'],
            issueType=request.POST['issueType'],
            exchange=request.POST['exchange'],
            description=request.POST['description'],
        )

        try:
            request.dbsession.add(instance)
        except DBAPIError:
            return Response(DB_ERROR_MSG, content_type='text/plain', status=500)

        return HTTPFound(location=request.route_url('entries'))
    if request.method == 'GET':
        return {}
    # if request.method == 'GET':
    #     try:
    #         symbol = request.GET['symbol']
    #     except KeyError:
    #         return {}

    #     response = requests.get(
    #         API_URL + '/stock/{}/company'.format(symbol))
    #     try:
    #         data = response.json()
    #         return {'company': data}
    #     except json.decoder.JSONDecodeError:
    #         return {'err': 'Invalid '}
    # else:
    #     raise HTTPNotFound()

