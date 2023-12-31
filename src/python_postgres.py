import psycopg2


conn = None
cur = None

try:

    conn = psycopg2.connect(
        user="postgres",
        password="3136",
        host="localhost",
        port="5432",
        database="postgres"
    )

    cur = conn.cursor()

    # Creating a table on Postgres
    create_script = ''' CREATE TABLE IF NOT EXISTS stock_dividends (
        ticker varchar (50),
        date varchar(50),
        dividends REAL NOT NULL,
        year INT NOT NULL
    ) '''

    cur.execute(create_script)

    # Manually inserting values into a table
    insert_script = ''' INSERT INTO stock_dividends
        (ticker, date, dividends, year) VALUES (%s, %s, %s, %s)'''

    insert_values = ('SNAG11', '2023-12-31', 32, 2023)
    cur.execute(insert_script, insert_values)

    conn.commit()
except Exception as error:
    print('Error: ', error)

finally:
    if cur is not None:
        cur.close()

    if conn is not None:
        conn.close()
