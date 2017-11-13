from ..services import db
from ..dao import celery_dao

def get_last_exports(id):
    con = None
    try:
        con = db.getconn()
        cur = con.cursor()
        param = celery_dao.get_last_exports(id, cur)
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
        if (form):
            rows = celery_dao.get_lists_row_without_price(param, cur)
        else:
            rows = celery_dao.get_lists_row_with_price(param, cur)
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
        celery_dao.update_exports(fname, id, cur)
        con.commit()
    finally:
        if con:
            cur.close()
            con.close()
            db.putconn(con)