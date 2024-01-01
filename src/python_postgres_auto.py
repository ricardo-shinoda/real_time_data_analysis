import psycopg2
from decouple import config
import yfinance as yf

cur = None
conn = None

user = config('user')
password = config('password')
host = config('host')
port = config('port')
database = config('database')

# Ticker symbol
ticker_symbols = ['PETR4.SA', 'SNAG11.SA', 'KLBN11.SA']
ticker_symbol = 'KLBN11.SA'  # Change to the desired ticker symbol

# Fetch ticker data
ticker = yf.Ticker(ticker_symbol)
stock_info = ticker.info

# Get dividend data
df = ticker.dividends
data = df.resample('Y').sum().reset_index()
data['Year'] = data['Date'].dt.year

try:
    conn = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database)

    cur = conn.cursor()

    create_script = ''' CREATE TABLE IF NOT EXISTS dividends_auto (
        date DATE PRIMARY KEY,
        dividends REAL NOT NULL,
        year INT NOT NULL)'''

    cur.execute(create_script)

except Exception as error:
    print('Error:', error)

try:
    insert_script = 'INSERT INTO dividends_auto (date, dividends, year) VALUES (%s, %s, %s)'

    for index, row in data.iterrows():
        values = (row['Date'], row['Dividends'], row['Year'])
        cur.execute(insert_script, values)
        conn.commit()

except Exception as error:
    print('Error: ', error)

finally:
    if cur is not None:
        cur.close()

    if conn is not None:
        conn.close()
