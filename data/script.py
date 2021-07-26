# pip install pandas
import csv
import psycopg2
import numpy as np
import pandas as pd


def process_data():
    df = pd.read_csv(r'./data/valeursfoncieres-2020.txt',
                     delimiter='|', decimal=',', na_values='', quoting=csv.QUOTE_NONNUMERIC)
    columns = [
        'Date mutation',  # indice 0
        'Valeur fonciere',  # 1
        'Code postal',  # 2
        'Code departement',  # 3
        'Code commune',  # 4
        'Code type local',  # 5
        'Surface reelle bati',  # 6
        'Nombre pieces principales',  # 7
        'Commune'  # 8
    ]
    df = df[columns]

    int_columns = [df.columns.difference(
        ['Date mutation', 'Commune', 'Code departement', 'Valeur fonciere'])]
    for col in int_columns:
        df[col] = (
            df[col].fillna(0)
            .astype(int)
            .astype(object)
            .where(df[col].notnull())
        )

    df.to_csv(r'./data/data.csv', index=False)
    print(f'File was stored : ./data/data.csv')


def connect():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='immo_db',
            user='postgres',
            password=''
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print('Connection established with postgres.')
        return conn


def queries():
    conn = connect()
    conn.autocommit = True

    file = open('./data/data.csv', "r")
    df = csv.reader(file, delimiter=',')

    cur = conn.cursor()
    for row in df:
        cur.execute("SET DATESTYLE TO 'ISO, DMY'")

        x = 0
        for row in df:
            cur.execute(
                'INSERT INTO commune (code_commune, commune) VALUES (%s, %s) ON CONFLICT DO NOTHING', (row[4], row[8]))

            cur.execute(
                'INSERT INTO localisation (code_postal, code_departement, code_commune) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING', (row[2] or None, row[3], row[4]))

            cur.execute(
                'INSERT INTO bien (code_type_local, surface_reel_bati, nb_pieces_principales, code_postal) VALUES (%s, %s, %s, %s) RETURNING id', (row[5] or None, row[6] or None, row[7] or None, row[2] or None))
            bien_id = cur.fetchone()[0]

            cur.execute(
                'INSERT INTO transaction (date_mutation, valeur_fonciere, bien_id) VALUES (%s, %s, %s)', (row[0], row[1] or None, bien_id))

            x += 1
            print(x)
            if x == 1000:
                cur.close()
                conn.close()
                exit()

    cur.close()
    conn.close()


# process_data()
queries()


conn = connect()
cur = conn.cursor()


# TESTS BELOW
# cur.execute(
#     "SELECT * FROM localisation JOIN commune on localisation.code_commune=commune.code_commune WHERE localisation.code_postal='1000000'"
# )
# l = cur.fetchall()

# gouv_cp_API_base = 'https://geo.api.gouv.fr/communes?nom='


# def complete_cp(list=[]):
#     for x in list:
#         print(x)


# complete_cp(l)


# SELECT * FROM transaction JOIN bien ON transaction.bien_id = bien.id JOIN localisation ON localisation.code_postal = bien.code_postal JOIN commune ON commune.code_commune = localisation.code_commune ORDER BY transaction.date_mutation
