import os
import psycopg2


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='Projekt_bazy',
                            user='postgres',   #os.environ['DB_USERNAME'],
                            password='root')  #os.environ['DB_PASSWORD'])
    return conn