from ..services import view_dao_services
import os
import os.path
from pyramid.response import FileResponse
from ..CeleryTasks  import *

def get_list():
    return view_dao_services.row_ret_lists()

def insert_export(TypeReport, dateS, dateF):
    id = view_dao_services.insert_exports(TypeReport, dateS, dateF)
    crrfil.delay(id)
  
def get_exports():
    return view_dao_services.row_ret_exports()

def download_start(request):
    if request.params.get('filename', ''):
        filename = request.params['filename']
        file_path = filename
        base_file_name = os.path.basename(file_path)
    response = FileResponse(file_path, request = request, cache_max_age=86400)
    headers = response.headers
    headers['Content-Type'] = 'application/download'
    headers['Accept-Ranges'] = 'bite'
    headers['Content-Disposition'] = 'attachment;filename=' +base_file_name
    return response

