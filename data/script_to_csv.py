# pip install pandas
import psycopg2
import pandas as pd


def process_data():
    df = pd.read_csv(r'./data/valeursfoncieres-2020.txt',
                     delimiter='|', decimal=',')
    columns = [
        'Date mutation',
        'Valeur fonciere',
        'Code postal',
        'Code departement',
        'Code commune',
        'Code type local',
        'Surface reelle bati',
        'Nombre pieces principales',
        'Commune'
    ]
    df = df[columns]
    int_columns = [df.columns.difference(
        ['Date mutation', 'Commune', 'Code departement'])]
    for col in int_columns:
        df[col] = (
            df[col].fillna(0)
            .astype(int)
            .astype(object)
            .where(df[col].notnull())
        )
    df.to_csv(r'./data/data.csv')


# pip install psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='immo_db',
            user='immo_admin',
            password='e5679489-a4c8-445a-9036-0838a70de506'
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print('Connection established with postgres.')
        return conn


process_data()
