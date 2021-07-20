BEGIN;

DROP TABLE IF EXISTS "transaction", "localisation", "bien", "commune" CASCADE;

CREATE TABLE bien (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    code_type_local INT,
    surface_reel_bati INT,
    nb_pieces_principales INT,
    code_postal INT NOT NULL,
    FOREIGN KEY(code_postal) REFERENCES localisation(code_postal)
);

CREATE TABLE localisation (
    code_postal INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    code_departement INT,
    code_commune INT,
    FOREIGN KEY(code_commune) REFERENCES commune(code_commune)
);

CREATE TABLE commune (
    code_commune INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    commune VARCHAR(255)
);

CREATE TABLE transaction (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    date_mutation DATE NOT NULL,
    valeur_fonciere INT NOT NULL,
    bien_id INT,
    FOREIGN KEY(bien_id) REFERENCES bien(id)
);

COMMIT;