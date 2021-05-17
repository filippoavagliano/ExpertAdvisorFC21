import MetaTrader5 as mt5

from utilscandles import get_last_candles, get_ocdistances, get_mMdistances

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
