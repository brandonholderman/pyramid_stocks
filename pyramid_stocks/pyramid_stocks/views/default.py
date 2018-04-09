from pyramid.response import Response
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..sample_data import MOCK_DATA
import requests
import json

from ..models import MyModel

API_URL = 'https://api.iextrading.com/1.0'

"""
Directs user to the home template
"""
@view_config(
route_name='home', 
renderer='../templates/base.jinja2', 
request_method='GET')
def index_view(request):
    return {}


"""
Directs user to authorization template and redirects to portfolio page on success
"""
@view_config(
route_name='auth', 
renderer='../templates/auth.jinja2')
def auth_view(request):
    try:
        if request.method == 'GET':
            username = request.GET['username']
            password = request.GET['password']
            print('User: {}, Pass: {}' .format(username, password))
            return HTTPFound(location=request.route_url('portfolio'))
    except KeyError:
        return {}
    
    if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            print('User: {}, Pass: {}, Email: {}' .format(username, password, email))
            return HTTPFound(location=request.route_url('portfolio'))
    return HTTPNotFound()

"""
Directs user to their portfolio template
"""
@view_config(
route_name='portfolio', 
renderer='../templates/portfolio.jinja2', 
request_method='GET')
def portfolio_view(request):
    return {'data' : API_URL,}


"""
Directs user to the add stock template
"""
@view_config(
route_name='add', 
renderer='../templates/add.jinja2', 
request_method='GET')
def add_view(request):
    if request.method == 'GET':
        try:
            symbol = request.GET['symbol']
        except KeyError:
            return {}

        response = requests.get(API_URL + '/stock/{}/company'.format(symbol))
        try:
            data = response.json()
            return {'company': data}
        except json.decoder.JSONDecodeError:
            return {'err': 'Invalid '}
    else:
        raise HTTPNotFound()

"""
Directs user to the detail template
"""
@view_config(
route_name='detail', 
renderer='../templates/detail.jinja2', 
request_method='GET')
def detail_view(request):
    symbol = request.matchdict['symbol']

    for data in API_URL:
        if data['symbol'] == symbol:
            return {'data': data}
    return {}
