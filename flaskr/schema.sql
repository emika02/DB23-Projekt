CREATE TABLE dokumenty (
    pracownicy_id_pracownik    INTEGER NOT NULL,
    specjalność_id_specjalnosc INTEGER NOT NULL
);

ALTER TABLE dokumenty ADD CONSTRAINT dokumenty_pk PRIMARY KEY ( pracownicy_id_pracownik,
                                                                specjalność_id_specjalnosc );

CREATE TABLE lokalizacja (
    id_lokalizacja    INTEGER NOT NULL,
    nazwa_lokalizacja VARCHAR(50) NOT NULL
);

ALTER TABLE lokalizacja ADD CONSTRAINT lokalizacja_pk PRIMARY KEY ( id_lokalizacja );

CREATE TABLE obszar (
    id_obszar                  INTEGER NOT NULL,
    nazwa_obszar               VARCHAR(50) NOT NULL,
    lokalizacja_id_lokalizacja INTEGER NOT NULL
);

ALTER TABLE obszar ADD CONSTRAINT obszar_pk PRIMARY KEY ( id_obszar );

CREATE TABLE prace (
    id_praca         INTEGER NOT NULL,
    nazwa_praca      VARCHAR(50) NOT NULL,
    obszar_id_obszar INTEGER
);

ALTER TABLE prace ADD CONSTRAINT prace_pk PRIMARY KEY ( id_praca );

CREATE TABLE pracownicy (
    id_pracownik INTEGER NOT NULL,
    imie         VARCHAR(50) NOT NULL,
    nazwisko     VARCHAR(50) NOT NULL
);

ALTER TABLE pracownicy ADD CONSTRAINT pracownicy_pk PRIMARY KEY ( id_pracownik );

CREATE TABLE specjalność (
    id_specjalnosc    INTEGER NOT NULL,
    nazwa_specjalnosc VARCHAR(50) NOT NULL
);

ALTER TABLE specjalność ADD CONSTRAINT specjalność_pk PRIMARY KEY ( id_specjalnosc );

CREATE TABLE zadanie (
    id_zadanie                 INTEGER NOT NULL,
    nazwa_zadanie              VARCHAR(50) NOT NULL,
    termin                     DATE NOT NULL,
    pracownicy_id_pracownik    INTEGER,
    specjalność_id_specjalnosc INTEGER,
    prace_id_praca             INTEGER NOT NULL
);

ALTER TABLE zadanie ADD CONSTRAINT zadanie_pk PRIMARY KEY ( id_zadanie );

ALTER TABLE dokumenty
    ADD CONSTRAINT dokumenty_pracownicy_fk FOREIGN KEY ( pracownicy_id_pracownik )
        REFERENCES pracownicy ( id_pracownik );

ALTER TABLE dokumenty
    ADD CONSTRAINT dokumenty_specjalność_fk FOREIGN KEY ( specjalność_id_specjalnosc )
        REFERENCES specjalność ( id_specjalnosc );

ALTER TABLE obszar
    ADD CONSTRAINT obszar_lokalizacja_fk FOREIGN KEY ( lokalizacja_id_lokalizacja )
        REFERENCES lokalizacja ( id_lokalizacja );

ALTER TABLE prace
    ADD CONSTRAINT prace_obszar_fk FOREIGN KEY ( obszar_id_obszar )
        REFERENCES obszar ( id_obszar );

ALTER TABLE zadanie
    ADD CONSTRAINT zadanie_prace_fk FOREIGN KEY ( prace_id_praca )
        REFERENCES prace ( id_praca );

ALTER TABLE zadanie
    ADD CONSTRAINT zadanie_pracownicy_fk FOREIGN KEY ( pracownicy_id_pracownik )
        REFERENCES pracownicy ( id_pracownik );

ALTER TABLE zadanie
    ADD CONSTRAINT zadanie_specjalność_fk FOREIGN KEY ( specjalność_id_specjalnosc )
        REFERENCES specjalność ( id_specjalnosc );

INSERT INTO specjalność 
VALUES (1,'sadzenie');

INSERT INTO specjalność 
VALUES (2,'kopanie');

INSERT INTO lokalizacja
VALUES (1,'Mokotów');

INSERT INTO lokalizacja
VALUES (2,'Praga');

INSERT INTO lokalizacja
VALUES (3,'Białołęka');

INSERT INTO obszar
VALUES (1,'Saska Kępa',2);

INSERT INTO obszar
VALUES (2,'Tarchomin',3);

INSERT INTO pracownicy
VALUES (1,'Tadeusz','Koza');

INSERT INTO prace
VALUES(1,'sadzenie drzew',1);

INSERT INTO dokumenty
VALUES(1,1);

INSERT INTO zadanie
VALUES(1,'przygotowanie nasion','2023-05-06',1,1,1);





