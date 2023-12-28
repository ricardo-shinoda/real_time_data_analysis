# This is going to be the place where I fetch the information from the api

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime


petro = yf.Ticker('petr4.sa')
print(petro.info)
