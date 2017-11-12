import psycopg2

HOST = 'localhost'
DBname = 'sec'
User = 'alt'
Password = '1234'

def row_ret_lists():
    con = None
    try:
        con = psycopg2.connect("host = {0} dbname ={1} user={2} password={3}".format(HOST, DBname, User, Password))
        cur = con.cursor()
        cur.execute("SELECT * FROM lists")
        rows = cur.fetchall()
    finally:
        if con:
            con.close()
    return rows

def insert_exports(TypeReport, dateS, dateF):
    con = None
    param = 0
    try:
        con = psycopg2.connect("host = {0} dbname ={1} user={2} password={3}".format(HOST, DBname, User, Password))
        cur = con.cursor()
        cur.execute("INSERT INTO exports (type, from_date, to_date, started) VALUES ( '{0}', '{1}', '{2}', now() ) RETURNING id;".format(TypeReport, dateS, dateF))
        con.commit()
        myid = cur.fetchall()
        param = myid[0]
    finally:
        if con:
            con.close()
    return param

def row_ret_exports():
    con = None
    try:
        con = psycopg2.connect("host = 'localhost' dbname ='sec' user='alt' password='1234'")
        cur = con.cursor()
        cur.execute("SELECT * FROM exports")
        rows = cur.fetchall()
    finally:
        if con:
            con.close()
    return rows