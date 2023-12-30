import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
import pandas as pd


def retrieve_historical_data(ticker, start_date, end_date):
    return ticker.history(start=start_date, end=end_date).Close


# Define ticker symbols and names
ticker_symbols = ['PETR4.SA', 'SNAG11.SA', 'KLBN4.SA',
                  'RBRP11.SA', 'AESB3F.SA', 'ITSA4.SA', 'GRND3.SA']
ticker_names = ['PETR4', 'SNAG11', 'KLBN4',
                'RBRP11', 'AESB3F', 'ITSA4', 'GRND3']

# Retrieve historical data
start_date = "2014-01-23"
end_date = datetime.now().date().strftime("%Y-%m-%d")
df = pd.DataFrame()

for symbol in ticker_symbols:
    ticker = yf.Ticker(symbol)
    df[ticker] = retrieve_historical_data(ticker, start_date, end_date)

# Plot the data
df.plot()
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.title('Stock Prices Over Time')
plt.legend(ticker_names)
plt.grid(True)
plt.tight_layout()
plt.show()
