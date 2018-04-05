from pyramid.response import Response
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from ..models import MyModel


@view_config(route_name='index', renderer='../templates/index.jinja2', request_method='GET')
def index_view(request):
    return Response('I did a thing')


@view_config(route_name='auth', renderer='../templates/auth.jinja2')
def auth_view(request):
    try:
        if request.method == 'GET':
            username = request.GET('username')
            password = request.GET('password')
            print('User: {}, Pass: {}' .format(username, password))
            return HTTPFound(location=request.route_url('index'))
    except KeyError:
        return {}
    
    if request.method == 'POST':
            username = request.POST('username')
            email = request.POST
            password = request.POST('password')
            print('User: {}, Pass: {}, Email: {}' .format(username, password, email))
            return HTTPFound(location=request.route_url('index'))
    return HTTPNotFound()

@view_config(route_name='portfolio', renderer='../templates/portfolio.jinja2', request_method='GET')
def portfolio_view(request):
    return {}


@view_config(route_name='add', renderer='../templates/add.jinja2', request_method='GET')
def add_view(request):
    return {}


@view_config(route_name='detail', renderer='../templates/detail.jinja2', request_method='GET')
def detail_view(request):
    return {}
