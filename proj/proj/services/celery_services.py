from ..services import db
from ..dao import celery_dao

def get_last_exports(id):
    con = None
    try:
        con = db.getconn()
        cur = con.cursor()
        param = celery_dao.get_last_exports(cur, id[0])
    except Exception as e:
        print(e)
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
            rows = celery_dao.get_lists_row_without_price(cur, param[0][1], param[0][2])
        else:
            rows = celery_dao.get_lists_row_with_price(cur, param[0][1], param[0][2])
    except Exception as e:
        print(e)
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
        celery_dao.update_exports(cur, fname, id[0])
        con.commit()
    except Exception as e:
        con.rollback()
        print(e)
    finally:
        if con:
            cur.close()
            con.close()
            db.putconn(con)