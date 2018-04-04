from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import MyModel


@view_config(route_name='index', renderer='../templates/index.jinja2')
def my_view(request):
    return {}
