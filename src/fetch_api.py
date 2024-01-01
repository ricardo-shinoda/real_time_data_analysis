import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
import pandas as pd
import psycopg2
from psycopg2 import Error

# Ticker symbol
ticker_symbols = ['PETR4.SA', 'SNAG11.SA', 'KLBN11.SA']
ticker_symbol = 'KLBN11.SA'  # Change to the desired ticker symbol

# Fetch ticker data
ticker = yf.Ticker(ticker_symbol)
stock_info = ticker.info

# Printing stock info
for key, value in stock_info.items():
    print(key, ":", value)

# Print dividends
print('Dividends:', ticker.dividends)

# Print current price
print('Current Price:', stock_info['currentPrice'])

# Print major holders
print('Major Holders:', ticker.major_holders)

# Print institutional holders
print('Institutional Holders:', ticker.institutional_holders)

# Get dividend data and plot
df = ticker.dividends
data = df.resample('Y').sum().reset_index()
data['Year'] = data['Date'].dt.year

plt.figure()
plt.bar(data['Year'], data['Dividends'])
plt.ylabel('Dividend Yield ($)')
plt.xlabel('Year')
plt.title(f'{ticker_symbol} Dividend History')
plt.xlim(2010, 2024)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
