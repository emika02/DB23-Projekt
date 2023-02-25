<h1>Projekt Zaliczeniowy - Bazy Danych i Usługi Sieciowe 22/23 MIM UW</h1>

**Emilia Kaczmarczyk, Indeks 440419**

**Opis projektu**

Program służący do zarządzania bazą pracowników ogrodu botanicznego z poziomu strony html.

**Instalacja i uruchamianie**

Projekt wymaga zainstalowanego języka Python 3.10 wraz z menadżerem paczek pip oraz PostgreSQL 14. Poniżej znajdują się kolejne komendy, jakie należy wprowadzić w linii poleceń, aby zainstalować wymagane paczki i uruchomić program, po uprzednim ściągnięciu i wejściu do folderu z plikami. Aby projekt działał poprawnie, najpierw należy zmienić dane połączenia w funkcji get_db_connection w pliku o tej samej nazwie (domyślnie użytkownik to postgres, a hasło to root). Jeśli program uruchamiany jest pierwszy raz, należy uruchomić plik setup_db.py (w innym wypadku należy pominąć tą komendę).
    
    pip install -r requirements.py
    cd flaskr
    set FLASK_APP=app.py
    set FLASK_ENV=development
    python setup_db.py
    python -m flask run --host=0.0.0.0
    
Strona wyświetlana jest na adresie http://127.0.0.1:5000 