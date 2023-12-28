#!/usr/bin/env python3
# This is going to be the place where I fetch the information from the api

import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')


petro = yf.Ticker('petr4.sa')
snag11 = yf.Ticker('snag11.sa')
klabin = yf.Ticker('klbn11.sa')

ticker = klabin

stockInfo = ticker.info


for key, value in stockInfo.items():
    print(key, ":", value)

# numbShares = petro.info['sharesOutstanding']
# currentPrice = snag11.info['currentPrice']
# print('The number of share are: ', numbShares)
# print('The Current Price per stock is:', currentPrice)

# to check the dividends
print(ticker.dividends)

print('Current Price:', stockInfo['currentPrice'])
# To know who the major holders are
print(ticker.major_holders)

# To know who the institutions are
print(ticker.institutional_holders)

df = petro.dividends
data = df.resample('Y').sum()
data = data.reset_index()

data['Year'] = data['Date'].dt.year
plt.figure()
plt.bar(data['Year'], data['Dividends'])
plt.ylabel('Dividend Yield ($)')
plt.xlabel('Year')
plt.title(f'{ticker.info["symbol"]} dividend history')
plt.xlim(2014, 2022)
plt.show()
