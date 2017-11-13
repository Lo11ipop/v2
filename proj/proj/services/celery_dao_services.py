from ..services import db
from ..dao import celery_dao
import datetime

def get_last_exports(id):
    con = None
    try:
        con = db.getconn()
        cur = con.cursor()
        try:
            param = celery_dao.get_last_exports(id[0], cur)
        except ValueError:
            param = celery_dao.get_last_exports(0, cur)
    finally:
        if con:
            cur.close()
            con.close()
            db.putconn(con)
    return param

def get_lists_row(param, form):
    con = None
    try:
        con = db.getconn()
        cur = con.cursor()
        try:
            if (form):
                rows = celery_dao.get_lists_row_without_price(param[0][1],param[0][2], cur)
            else:
                rows = celery_dao.get_lists_row_with_price(param[0][1],param[0][2], cur)
        except TypeError:
            if (form):
                rows = celery_dao.get_lists_row_without_price(datetime.datetime.now()-datetime.timedelta(days=1),datetime.datetime.now()+datetime.timedelta(days=1), cur)
            else:
                rows = celery_dao.get_lists_row_with_price(datetime.datetime.now()-datetime.timedelta(days=1),datetime.datetime.now()+datetime.timedelta(days=1), cur)
    finally:
        if con:
            cur.close()
            con.close()
            db.putconn(con)
    return rows

def update_exports(fname, id):
    con = None
    try:
        con = db.getconn()
        cur = con.cursor()
        try:
            celery_dao.update_exports(fname, id[0], cur)
            con.commit()
        except Exception:
            con.rollback()
    finally:
        if con:
            cur.close()
            con.close()
            db.putconn(con)