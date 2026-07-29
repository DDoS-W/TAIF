"""
Feature Builder

TAIF
"""

import pandas as pd

from .indicators import (
    moving_average,
    daily_return,
    rolling_volatility,
    rsi
)


class FeatureBuilder:

    def __init__(self):

        pass

    def build(self, df: pd.DataFrame):

        feature_df = df.copy()

        # Moving Average
        feature_df["MA5"] = moving_average(
            feature_df["Close"], 5
        )

        feature_df["MA20"] = moving_average(
            feature_df["Close"], 20
        )

        # Daily Return
        feature_df["DailyReturn"] = daily_return(
            feature_df["Close"]
        )

        # Volatility
        feature_df["Volatility20"] = rolling_volatility(
            feature_df["DailyReturn"], 20
        )

        # RSI
        feature_df["RSI14"] = rsi(
            feature_df["Close"], 14
        )

        return feature_df
