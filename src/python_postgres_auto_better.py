import psycopg2
from contextlib import closing
import yfinance as yf
import logging
from decouple import config

# Configure the logging module
logging.basicConfig(filename='database.log', level=logging.INFO)


def main():
    user = config('user')
    password = config('password')
    host = config('host')
    port = config('port')
    database = config('database')

    try:
        with closing(psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )) as conn:
            with conn.cursor() as cur:
                create_table_if_not_exists(cur)
                insert_dividends_data(cur, conn)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print("An error occurred: ", e)


def create_table_if_not_exists(cur):
    create_script = '''CREATE TABLE IF NOT EXISTS dividends_auto3 (
        date DATE PRIMARY KEY,
        dividends REAL NOT NULL,
        year INT NOT NULL)'''
    cur.execute(create_script)


def insert_dividends_data(cur, conn):
    ticker_symbol = 'SNAG11.SA'
    ticker = yf.Ticker(ticker_symbol)
    df = ticker.dividends
    data = df.resample('Y').sum().reset_index()
    data['Year'] = data['Date'].dt.year

    insert_script = 'INSERT INTO dividends_auto3 (date, dividends, year) VALUES (%s, %s, %s)'
    for index, row in data.iterrows():
        values = (row['Date'], row['Dividends'], row['Year'])
        cur.execute(insert_script, values)
        conn.commit()  # Commit once at the end of the loop


if __name__ == "__main__":
    main()
