from ..services import db
from ..dao import view_dao

def row_ret_lists():
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

def insert_exports(TypeReport, dateS, dateF):
    con = None
    param = 0
    try:
        con = db.getconn()
        cur = con.cursor()
        myid = view_dao.insert_exports(TypeReport, dateS, dateF, cur)
        con.commit()
        param = myid[0]
    finally:
        if con:
            cur.close()
            con.close()
            db.putconn(con)
    return param

def row_ret_exports():
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