import os
import psycopg2
from flask import Flask, render_template
from flask import request, url_for, redirect
import pyodbc

from get_db_connection import get_db_connection


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM zadanie ORDER BY id_zadanie ASC;')
    zadanie = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', zadanie=zadanie)

@app.route('/wolne_zadania/')
def wolne_zadania():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM zadanie WHERE pracownicy_id_pracownik IS NULL ORDER BY termin ASC;')
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
    cur.execute('SELECT * FROM pracownicy ORDER BY id_pracownik ASC;')
    pracownicy = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index_pracownicy.html', pracownicy=pracownicy)

@app.route('/lokalizacja/')
def index_lokalizacja():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM lokalizacja ORDER BY id_lokalizacja ASC;')
    lokalizacja = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index_lokalizacja.html',lokalizacja=lokalizacja)

@app.route('/obszar/')
def index_obszar():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM obszar ORDER BY id_obszar ASC;')
    obszar = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index_obszar.html',obszar=obszar)

@app.route('/prace/')
def index_prace():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM prace ORDER BY id_praca ASC;')
    prace = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index_prace.html',prace=prace)

@app.route('/specjalność/')
def index_specjalność():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM specjalność ORDER BY id_specjalnosc ASC;')
    specjalność = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index_specjalność.html',specjalność=specjalność)
    
@app.route('/create_zp/', methods=('GET', 'POST'))
def create_zp():
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

    return render_template('create_zp.html')

@app.route('/create_bp/', methods=('GET', 'POST'))
def create_bp():
    if request.method == 'POST':
        id_zadanie = int(request.form['id_zadanie'])
        nazwa_zadanie = request.form['nazwa_zadanie']
        termin = request.form['termin']
        specjalność_id_specjalnosc= int(request.form['specjalność_id_specjalnosc'])
        prace_id_praca= int(request.form['prace_id_praca'])

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO zadanie (id_zadanie, nazwa_zadanie, termin, specjalność_id_specjalnosc,prace_id_praca)'
                    'VALUES (%s, %s, %s, %s,%s)',
                    (id_zadanie,nazwa_zadanie,termin,specjalność_id_specjalnosc,prace_id_praca))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create_bp.html')

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

@app.route('/create_obszar/', methods=('GET', 'POST'))
def create_obszar():
    if request.method == 'POST':
        id_obszar = int(request.form['id_obszar'])
        nazwa_obszar= request.form['nazwa_obszar']
        lokalizacja_id_lokalizacja = int(request.form['lokalizacja_id_lokalizacja'])
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO obszar(id_obszar, nazwa_obszar,lokalizacja_id_lokalizacja)'
                    'VALUES (%s, %s,%s)',
                    (id_obszar,nazwa_obszar,lokalizacja_id_lokalizacja))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index_obszar'))

    return render_template('create_obszar.html')

@app.route('/create_prace/', methods=('GET', 'POST'))
def create_prace():
    if request.method == 'POST':
        id_praca = int(request.form['id_praca'])
        nazwa_praca= request.form['nazwa_praca']
        obszar_id_obszar = int(request.form['obszar_id_obszar'])
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO prace(id_praca,nazwa_praca,obszar_id_obszar)'
                    'VALUES (%s, %s,%s)',
                    (id_praca,nazwa_praca,obszar_id_obszar))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index_prace'))

    return render_template('create_prace.html')

@app.route('/create_specjalność/', methods=('GET', 'POST'))
def create_specjalność():
    if request.method == 'POST':
        id_specjalnosc = int(request.form['id_specjalnosc'])
        nazwa_specjalnosc= request.form['nazwa_specjalnosc']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO prace(id_specjalnosc,nazwa_specjalnosc)'
                    'VALUES (%s, %s)',
                    (id_specjalnosc,nazwa_specjalnosc))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index_specjalność'))

    return render_template('create_specjalność.html')


@app.route('/edit_termin/', methods=('GET', 'POST'))
def edit_termin():
    if request.method == 'POST':
        id_zadanie = int(request.form['id_zadanie'])
        nowy_termin = request.form['nowy_termin']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE zadanie SET termin = (%s)'
                    'WHERE id_zadanie = (%s) AND termin NOT IN (SELECT termin FROM Zadanie WHERE Pracownicy_id_pracownik IN (SELECT Pracownicy_id_pracownik FROM zadanie WHERE id_zadanie = (%s)))',
                    (nowy_termin, id_zadanie,id_zadanie)
                    )
   
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('edit_termin.html')

@app.route('/edit_pracownik/', methods=('GET', 'POST'))
def edit_pracownik():
    if request.method == 'POST':
        id_zadanie = int(request.form['id_zadanie'])
        pracownicy_id_pracownik = request.form['id_pracownik']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE zadanie SET pracownicy_id_pracownik = (%s)'
                    'WHERE id_zadanie = (%s)  AND termin NOT IN (SELECT termin FROM zadanie WHERE pracownicy_id_pracownik = (%s))',
                    (pracownicy_id_pracownik, id_zadanie,pracownicy_id_pracownik)
                    )
   
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('edit_pracownik.html')



# if running this module as a standalone program (cf. command in the Python Dockerfile)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)