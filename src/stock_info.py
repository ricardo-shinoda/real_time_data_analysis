import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf


def retrieve_stock_info(ticker):
    stock_info = ticker.info
    print("Cashflow information:")
    print(ticker.cashflow)
    print("Historical data (period='max'):")
    print(ticker.history(period='max'))
    return stock_info


def plot_stock_price(ticker, start_date, end_date):
    df = ticker.history(start=start_date, end=end_date)
    plt.figure()
    plt.plot(df['Close'])
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.title('Stock Price Over Time')
    plt.grid(True)
    plt.show()


# Define the tickers and select one for analysis
tickers = ['PETR4.SA', 'SNAG11.SA', 'KLBN11.SA']
ticker = yf.Ticker('PETR4.SA')

# Retrieve stock information and print to console
stock_info = retrieve_stock_info(ticker)

# Define the time range for plotting
start_date = "2019-01-23"
end_date = datetime.now().date().strftime("%Y-%m-%d")

# Plot the stock prices
plot_stock_price(ticker, start_date, end_date)
