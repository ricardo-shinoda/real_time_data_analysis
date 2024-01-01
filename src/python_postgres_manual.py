import psycopg2
from decouple import config

cur = None
conn = None

user = config('user')
password = config('password')
host = config('host')
port = config('port')
database = config('database')

try:
    conn = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database)

    cur = conn.cursor()

    create_script = ''' CREATE TABLE IF NOT EXISTS dividends (
        ticker varchar(100),
        date DATE PRIMARY KEY,
        dividends REAL NOT NULL,
        year INT NOT NULL)'''

    cur.execute(create_script)

    insert_script = 'INSERT INTO dividends (ticker, date, dividends, year) VALUES (%s, %s, %s, %s)'
    insert_values = [("SNAG11", "2023-12-30", 30, 2023),
                     ("PETR4", "2022-12-29", 31, 2022)]

    cur.executemany(insert_script, insert_values)

    conn.commit()
except Exception as error:
    print('Error:', error)

finally:
    if cur is not None:
        cur.close()

    if conn is not None:
        conn.close()
