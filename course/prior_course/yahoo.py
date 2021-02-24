import datetime as dtm
import numpy as np
import statsmodels.formula.api as smd
import pandas as pd
import pandas_datareader.data as pdr
from pandas import DataFrame
import yfinance
import rebiber

tickers = ['AAPL', 'BABA', 'IBM', 'MSFT', 'GOOGL', 'GME']
# end = dtm.date(2020, 12, 1)
# start = dtm.date(2019, 11, 29)
# ff_factors = pdr.DataReader('F-F_Research_Data_5_Factors_2x3_daily', 'famafrench', start, end)[0]
# yfinance.pdr_override()
# all_data = {}
# for ticker in tickers:
#     all_data[ticker] = pdr.get_data_yahoo(ticker, start, end)
# price = DataFrame({tic: all_data[tic]['Adj Close'] for tic in all_data})
# price.to_csv('../data/all_data.csv')
# ff_factors.to_csv('../data/ff_factors.csv')

price = pd.read_csv('../../data/all_data.csv')
price.index = [dtm.datetime.strptime(str(x), "%Y-%m-%d") for x in price.iloc[:, 0]]
price = price.iloc[:, 1:]
log_prices = []
for ticker in tickers:
    log_prices.append(np.log(price[ticker]).diff().dropna())
df = pd.concat(log_prices, axis=1).dropna()
df.columns = tickers

ff_factors = pd.read_csv('../../data/ff_factors.csv')
ff_factors.index = [dtm.datetime.strptime(str(x), "%Y-%m-%d") for x in ff_factors.iloc[:, 0]]
ff_factors = ff_factors.iloc[:, 1:]
ff_factors = ff_factors.rename(columns={'Mkt-RF': 'MKT'})
ff_factors = ff_factors.apply(lambda x: x / 100)
for idx, log_price in enumerate(log_prices):
    ff_price = pd.concat([ff_factors, log_price], axis=1)
    ff_model = smd.ols(formula=tickers[idx] + '~MKT+SMB+HML+RMW+CMA', data=ff_price).fit()
    print(ff_model.summary())
