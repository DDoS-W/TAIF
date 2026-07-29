"""
TAIF Indicators Module

Author: SHENG HSU
"""


import pandas as pd


def moving_average(series, window):

    """
    Moving Average

    Parameters
    ----------
    series : pd.Series

    window : int

    """

    return series.rolling(window).mean()

def daily_return(series):
    return series.pct_change()

def rolling_volatility(return_series, window=20):
    return return_series.rolling(window).std()

def rsi(series, period=14):

    delta = series.diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()

    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))
