from typing import List
from Candle import Candle


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

    return ema
