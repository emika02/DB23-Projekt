import os
import psycopg2

from get_db_connection import get_db_connection

conn = get_db_connection()
cur = conn.cursor()
cur.execute(open("flaskr\schema.sql", "r").read())

conn.commit()
cur.close()
conn.close()
