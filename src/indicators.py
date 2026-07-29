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
