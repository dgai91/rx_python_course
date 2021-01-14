import datetime as dtm

import pandas_datareader.data as pdr
from pandas import DataFrame
import pandas as pd
import yfinance

end = dtm.date(2020, 11, 30)
start = dtm.date(end.year - 1, end.month, end.day)
# ff_factors = pdr.DataReader('F-F_Research_Data_5_Factors_2x3_daily', 'famafrench', start, end)[0]
# ff_factors.to_csv('ff_factors.csv')
# yfinance.pdr_override()
# tickers = ['AAPL', 'BABA', 'IBM', 'MSFT', 'GOOGL', 'GME']
# all_data = {}
# for ticker in tickers:
#     all_data[ticker] = pdr.get_data_yahoo(ticker, start, end)
# price = DataFrame({tic: all_data[tic]['Adj Close'] for tic in all_data})
# price.to_csv('all_data.csv')

ff_factors = pd.read_csv('../data/ff_factors.csv')
price = pd.read_csv('../data/all_data.csv')
