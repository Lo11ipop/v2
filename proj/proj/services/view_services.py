import os
import os.path
from pyramid.response import FileResponse
from ..CeleryTasks  import *
from ..services import db
from ..dao import view_dao

def get_list():
    con = None
    try:
        con = db.getconn()
        cur = con.cursor()
        rows = view_dao.row_ret_lists(cur)
    finally:
        if con:
            cur.close()
            con.close()
            db.putconn(con)
    return rows

def insert_export(TypeReport, dateS, dateF):
    con = None
    param = 0
    try:
        con = db.getconn()
        cur = con.cursor()
        try:
            myid = view_dao.insert_exports(TypeReport, dateS, dateF, cur)
            con.commit()
            crrfil.delay(myid[0])
        except Exception:
            con.rollback()
            crrfil.delay(param)
    finally:
        if con:
            cur.close()
            con.close()
            db.putconn(con)

def get_exports():
    con = None
    try:
        con = db.getconn()
        cur = con.cursor()
        rows = view_dao.row_ret_exports(cur)
    finally:
        if con:
            cur.close()
            con.close()
            db.putconn(con)
    return rows

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

