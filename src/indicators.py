"""
TAIF Indicators Module

Reusable financial indicators.
"""

import pandas as pd


def moving_average(series: pd.Series, window: int) -> pd.Series:
    """
    Calculate moving average.
    """
    return series.rolling(window=window).mean()


def daily_return(series: pd.Series) -> pd.Series:
    """
    Calculate daily percentage return.
    """
    return series.pct_change()


def rolling_volatility(
    return_series: pd.Series,
    window: int = 20
) -> pd.Series:
    """
    Calculate rolling volatility.
    """
    return return_series.rolling(window=window).std()


def rsi(
    series: pd.Series,
    period: int = 14
) -> pd.Series:
    """
    Calculate Relative Strength Index (RSI).
    """

    delta = series.diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()

    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))
