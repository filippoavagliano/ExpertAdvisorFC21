import MetaTrader5 as mt5

from utilscandles import get_last_candles, get_ocdistances, get_mMdistances
from utils import get_ema, get_bollinger_band
from mt5api import get_bars

if __name__ == '__main__':
    symbol = "EURUSD"
    timeframe = mt5.TIMEFRAME_H1
    num_of_candles = 20

    candles = get_last_candles(num_of_candles, symbol, timeframe)

    print("Candele")
    [print(x) for x in candles]

    print()

    print("ocdistances")
    print(get_ocdistances(candles))

    print()

    print("mMdistances")
    print(get_mMdistances(candles))

    bars = get_bars(symbol, timeframe, num_of_candles)
    sma, lower, upper = get_bollinger_band(bars, 20)

    print(lower)
