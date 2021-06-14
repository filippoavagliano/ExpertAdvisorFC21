from typing import List
from Candle import Candle

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_ema(s: List[Candle], n) -> List:
    """
    returns an n period exponential moving average for
    the time series s

    s is a list ordered from oldest (index 0) to most
    recent (index -1)
    n is an integer

    returns a numeric array of the exponential
    moving average
    """

    print(" quante candele?: ", s.__len__())
    # s = array(s)
    ema = []
    j = 1


    # get n sma first and calculate the next n period ema
    sma = sum(c.close for c in s) / n
    multiplier = 2 / float(1 + n)
    ema.append(sma)

    # EMA(current) = ( (Price(current) - EMA(prev) ) x Multiplier) + EMA(prev)
    ema.append(((s[n].close - sma) * multiplier) + sma)


    # now calculate the rest of the values
    for i in s[n + 1:]:
        tmp = ((i.close - ema[j]) * multiplier) + ema[j]
        j = j + 1
        ema.append(tmp)

    print("\nARRAY EMA IN UTILS: " , ema)


    return ema

# def exponentialMovingAverage(data: List[Candle], num):
#     if (num > len(data)):
#         raise Exception('Insufficient data for calculation')
#
#     data_list = (c.close for c in data)
#     last_sma = -1
#     result = {}
#     for x in range(len(data_list) - num + 1):
#         series = data_list[x:x + num]
#         if (last_sma == -1):
#             result[data_keys[x + num - 1]] = round((sum(series) / num), 2)
#         else:
#             current_price = data[data_keys[x + num - 1]]
#             result[data_keys[x + num - 1]] = round(current_price * 2 / (num + 1) + last_sma * (1 - 2 / (num + 1)), 2)
#         last_sma = result[data_keys[x + num - 1]]
#
#     return result

def ema(values: List[Candle], period):
    values = np.array(c.close for c in values)
    print("return ema: ", pd.ewma(values, span=period)[-1])
    return pd.ewma(values, span=period)[-1]

def calculate_ema(prices : List[Candle], days, smoothing = 2):
    price_Int = list(c.close for c in prices)
    print("\n prezzi: ", price_Int)
    ema = [sum(price_Int[:days]) / days]
    for price in price_Int[days:]:
        ema.append((price * (smoothing / (1 + days))) + ema [-1] * (1 - (smoothing / (1 + days))))
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
