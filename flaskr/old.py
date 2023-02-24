from flask import Flask
import psycopg2

 # creates an application that is named after the name of the file
app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect("postgresql://postgres:root@localhost:5432/Projekt_bazy")
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT * FROM specjalność")
    
    # Retrieve query results
    records = cur.fetchall()
    
    cur.close()
    conn.close()

    return records

# if running this module as a standalone program (cf. command in the Python Dockerfile)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)