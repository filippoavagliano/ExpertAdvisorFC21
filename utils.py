from typing import List
from Candle import Candle

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def calculate_ema(prices : List[Candle], n, smoothing = 2):
    price_Int = list(c.close for c in prices)
    print("\n prezzi: ", price_Int, price_Int.__len__())
    ema = [sum(price_Int[:n]) / n]
    for price in price_Int[n:]:
        ema.append((price * (smoothing / (1 + n))) + ema [-1] * (1 - (smoothing / (1 + n))))
    print("ema ", ema)
    return ema

def get_bollinger_band(bars: pd.DataFrame, period: int):
    """
    Calculate the 20 Day Simple Moving Average, Upper Band and Lower Band
    :param bars: barre ottenute da MetaTrader 5
    :param period: time period in days
    :return: (sma, lower, upper)
    """
    # Calculating the Simple Moving Average
    bars['SMA'] = bars['close'].rolling(window=period).mean()

    # Get the standard deviation
    bars['STD'] = bars['close'].rolling(window=period).std()

    # Calculate the Upper Bollinger Band
    bars['Upper'] = bars['SMA'] + (bars['STD'] * 2)

    # Calculate the Lower Bollinger Band
    bars['Lower'] = bars['SMA'] - (bars['STD'] * 2)

    sma = bars['SMA'].to_list()
    upper = bars['Upper'].to_list()
    lower = bars['Lower'].to_list()

    return sma, lower, upper


def plot_bollinger_band(close, sma, lower, upper):
    column_list = ['Close', 'SMA', 'Lower', 'Upper']
    data = list(zip(close, sma, lower, upper))

    df = pd.DataFrame(data, columns=column_list)

    df[column_list].plot(figsize=(12.2, 6.4))  # Plot the data
    plt.title('Bollinger Band')
    plt.ylabel('USD Price ($)')
    plt.show()

    print(sma)
    print(lower)
