import os
import psycopg2
from flask import Flask, render_template
from flask import request, url_for, redirect


app = Flask(__name__, template_folder='templates')

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='Projekt_bazy',
                            user='postgres',#os.environ['DB_USERNAME'],
                            password='root')#os.environ['DB_PASSWORD'])
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM zadanie;')
    zadanie = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', zadanie=zadanie)

@app.route('/dokumenty/')
def index_dokumenty():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM dokumenty;')
    dokumenty = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index_dokumenty.html', dokumenty=dokumenty)

@app.route('/pracownicy/')
def index_pracownicy():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pracownicy;')
    pracownicy = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index_pracownicy.html', pracownicy=pracownicy)

@app.route('/lokalizacja/')
def index_lokalizacja():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM lokalizacja;')
    lokalizacja = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index_lokalizacja.html',lokalizacja=lokalizacja)
    
    
#adding new records



@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        id_zadanie = int(request.form['id_zadanie'])
        nazwa_zadanie = request.form['nazwa_zadanie']
        termin = request.form['termin']
        pracownicy_id_pracownik= int(request.form['pracownicy_id_pracownik'])
        specjalność_id_specjalnosc= int(request.form['specjalność_id_specjalnosc'])
        prace_id_praca= int(request.form['prace_id_praca'])

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO zadanie (id_zadanie, nazwa_zadanie, termin, pracownicy_id_pracownik, specjalność_id_specjalnosc,prace_id_praca)'
                    'VALUES (%s, %s, %s, %s,%s,%s)',
                    (id_zadanie,nazwa_zadanie,termin,pracownicy_id_pracownik,specjalność_id_specjalnosc,prace_id_praca))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/create_dokumenty/', methods=('GET', 'POST'))
def create_dokumenty():
    if request.method == 'POST':
        pracownicy_id_pracownik = int(request.form['pracownicy_id_pracownik'])
        specjalność_id_specjalnosc= int(request.form['specjalność_id_specjalnosc'])

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO dokumenty(pracownicy_id_pracownik, specjalność_id_specjalnosc)'
                    'VALUES (%s, %s)',
                    (pracownicy_id_pracownik,specjalność_id_specjalnosc))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index_dokumenty'))

    return render_template('create_dokumenty.html')

@app.route('/create_pracownicy/', methods=('GET', 'POST'))
def create_pracownicy():
    if request.method == 'POST':
        id_pracownik = int(request.form['id_pracownik'])
        imie= request.form['imie']
        nazwisko= request.form['nazwisko']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO pracownicy(id_pracownik, imie, nazwisko)'
                    'VALUES (%s, %s,%s)',
                    (id_pracownik,imie,nazwisko))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index_pracownicy'))

    return render_template('create_pracownicy.html')

@app.route('/create_lokalizacja/', methods=('GET', 'POST'))
def create_lokalizacja():
    if request.method == 'POST':
        id_lokalizacja = int(request.form['id_lokalizacja'])
        nazwa_lokalizacja= request.form['nazwa_lokalizacja']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO lokalizacja(id_lokalizacja, nazwa_lokalizacja)'
                    'VALUES (%s, %s)',
                    (id_lokalizacja, nazwa_lokalizacja))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index_lokalizacja'))

    return render_template('create_lokalizacja.html')

# if running this module as a standalone program (cf. command in the Python Dockerfile)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)