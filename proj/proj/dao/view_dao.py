from ..dao import db

def row_ret_lists():
    con = None
    try:
        con = db.getconn()
        cur = con.cursor()
        cur.execute("SELECT * FROM lists")
        rows = cur.fetchall()
    finally:
        if con:
            db.putconn(con)
    return rows

def insert_exports(TypeReport, dateS, dateF):
    con = None
    param = 0
    try:
        con = db.getconn()
        cur = con.cursor()
        cur.execute("INSERT INTO exports (type, from_date, to_date, started) VALUES ( '{0}', '{1}', '{2}', now() ) RETURNING id;".format(TypeReport, dateS, dateF))
        con.commit()
        myid = cur.fetchall()
        param = myid[0]
    finally:
        if con:
            db.putconn(con)
    return param

def row_ret_exports():
    con = None
    try:
        con = db.getconn()
        cur = con.cursor()
        cur.execute("SELECT * FROM exports")
        rows = cur.fetchall()
    finally:
        if con:
            db.putconn(con)
    return rows