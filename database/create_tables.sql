-- CLI : psql postgres -d immo_db < ./database/create_tables.sql

BEGIN;

DROP TABLE IF EXISTS "transaction", "localisation", "bien", "commune" CASCADE;

CREATE TABLE commune (
    code_commune VARCHAR(255) UNIQUE NOT NULL PRIMARY KEY,
    commune VARCHAR(255) NOT NULL
);

CREATE TABLE localisation (
    code_postal INT,
    code_departement VARCHAR(255) NOT NULL,
    code_commune VARCHAR(255) NOT NULL,

    CONSTRAINT code_postal_PK UNIQUE(code_postal)
);

CREATE TABLE bien (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    code_type_local INT,
    surface_reel_bati INT,
    nb_pieces_principales INT,
    code_postal INT NULL,
    FOREIGN KEY(code_postal) REFERENCES localisation(code_postal)
);


CREATE TABLE transaction (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    date_mutation DATE NOT NULL,
    valeur_fonciere FLOAT NULL,
    bien_id INT,
    FOREIGN KEY(bien_id) REFERENCES bien(id)
);

COMMIT;