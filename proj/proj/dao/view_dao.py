def row_ret_lists(cur):
    cur.execute("SELECT * FROM lists")
    return cur.fetchall()

def insert_exports(TypeReport, dateS, dateF, cur):
    cur.execute("INSERT INTO exports (type, from_date, to_date, started) VALUES ( '{0}', '{1}', '{2}', now() ) RETURNING id;".format(TypeReport, dateS, dateF))
    return cur.fetchall()

def row_ret_exports(cur):
    cur.execute("SELECT * FROM exports")
    return cur.fetchall()