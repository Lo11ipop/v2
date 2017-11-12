import psycopg2

HOST = 'localhost'
DBname = 'sec'
User = 'alt'
Password = '1234'

def get_last_exports(id):
    con = None
    try:
        con = psycopg2.connect("host = {0} dbname ={1} user={2} password={3}".format(HOST, DBname, User, Password))
        cur = con.cursor()
        cur.execute("SELECT type, from_date, to_date FROM exports WHERE id = '{0}';".format(id[0]))
        param = cur.fetchall()
    finally:
        if con:
            con.close()
    return param

def get_lists_row(param, form):
    con = None
    try:
        con = psycopg2.connect("host = {0} dbname ={1} user={2} password={3}".format(HOST, DBname, User, Password))
        cur = con.cursor()
        if(form):
            cur.execute("SELECT Name, created, updated  FROM lists WHERE '{0}' <= created AND '{1}' >= created;".format(param[0][1], param[0][2]))
            rows = cur.fetchall()
        else:
            cur.execute("SELECT Name, price, created, updated  FROM lists WHERE '{0}' <= created AND '{1}' >= created;".format(param[0][1], param[0][2]))
            rows = cur.fetchall()
    finally:
        if con:
            con.close()
    return rows

def update_exports(fname, id):
    con = None
    try:
        con = psycopg2.connect("host = {0} dbname ={1} user={2} password={3}".format(HOST, DBname, User, Password))
        cur = con.cursor()
        print(id)
        cur.execute("UPDATE exports SET path='{0}' WHERE id='{1}'".format(fname, id[0]))
        con.commit()
        cur.execute("UPDATE exports SET finished=now() WHERE id='{0}'".format(id[0]))
        con.commit()
    finally:
        if con:
            con.close()