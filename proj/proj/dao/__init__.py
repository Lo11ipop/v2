from psycopg2 import pool

HOST = 'localhost'
DBname = 'sec'
User = 'alt'
Password = '1234'

db = pool.ThreadedConnectionPool(1, 10, host=HOST, database=DBname, user=User, password=Password)

