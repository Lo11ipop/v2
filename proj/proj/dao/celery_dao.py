def get_last_exports(id, cur):
    cur.execute("SELECT type, from_date, to_date FROM exports WHERE id = {0};".format(id[0]))
    return cur.fetchall()

def get_lists_row_without_price(param, cur):
    cur.execute("SELECT Name, created, updated  FROM lists WHERE '{0}' <= created AND '{1}' >= created;".format(param[0][1], param[0][2]))
    return cur.fetchall()

def get_lists_row_with_price(param, cur):
    cur.execute("SELECT Name, price, created, updated  FROM lists WHERE '{0}' <= created AND '{1}' >= created;".format(param[0][1], param[0][2]))
    return cur.fetchall()

def update_exports(fname, id, cur):
    cur.execute("UPDATE exports SET path='{0}', finished=now() WHERE id= {1}".format(fname, id[0]))
