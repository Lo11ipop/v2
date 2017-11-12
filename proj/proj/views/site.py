from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from ..services import view_services

import datetime


@view_config(route_name = 'home', renderer='templates/home.jinja2')
def view_home(request):
    return {}

@view_config(route_name = 'list', renderer='templates/list.jinja2')
def view_list(request):
    return {'rows': view_services.get_list()}

@view_config(route_name = 'fexports', renderer='string')
def view_fexports(request):
    dateS = datetime.datetime.strptime(request.params['datepickerS'], '%m/%d/%Y')
    dateF = datetime.datetime.strptime(request.params['datepickerF'], '%m/%d/%Y')
    TypeReport = request.params['selecTyp']
    view_services.insert_export(TypeReport, dateS, dateF)
    return HTTPFound(location=request.route_url('exports'))

@view_config(route_name = 'exports', renderer='templates/exports.jinja2')
def view_exports(request):
    return {'rows': view_services.get_exports()}

@view_config(route_name='download')
def download_view(request):
    return view_services.download_start(request)