def get_last_exports(cur, id):
    cur.execute("SELECT type, from_date, to_date FROM exports WHERE id = {0};".format(id))
    return cur.fetchall()

def get_lists_row_without_price(cur, date_from, date_to):
    cur.execute("SELECT Name, created, updated  FROM lists WHERE '{0}' <= created AND '{1}' >= created;".format(date_from, date_to))
    return cur.fetchall()

def get_lists_row_with_price(cur, date_from, date_to):
    cur.execute("SELECT Name, price, created, updated  FROM lists WHERE '{0}' <= created AND '{1}' >= created;".format(date_from, date_to))
    return cur.fetchall()

def update_exports(cur, fname, id):
    cur.execute("UPDATE exports SET path='{0}', finished=now() WHERE id= {1}".format(fname, id))
