from pyramid.response import Response
from pyramid.view import view_config

from ..models import MyModel


@view_config(route_name='index', renderer='../templates/index.jinja2', request_method='GET')
def index_view(request):
    return {}


@view_config(route_name='auth', renderer='../templates/auth.jinja2', request_method='GET')
def auth_view(request):
    return {}


@view_config(route_name='portfolio', renderer='../templates/portfolio.jinja2', request_method='GET')
def portfolio_view(request):
    return {}


@view_config(route_name='add', renderer='../templates/add.jinja2', request_method='GET')
def add_view(request):
    return {}


@view_config(route_name='detail', renderer='../templates/detail.jinja2', request_method='GET')
def detail_view(request):
    return {}
