import MetaTrader5 as mt5
from PatternDetector import addCandleToVector, determinePatterns
from GenCandle import GenCandle
from mt5api import get_bars
from utils import get_ema, get_bollinger_band
from utilscandles import get_last_candles, extract_last_candles, get_ocdistances, get_mMdistances


def main():
    symbol = "EURUSD"
    timeframe = mt5.TIMEFRAME_H1
    num_of_candles = 29

    bars = get_bars(symbol, timeframe, num_of_candles)
    candles = extract_last_candles(bars, num_of_candles)

    bars = bars[:-1]
    last_candles = candles[:-1]

    print(bars)
    # bande di bollinger
    _, lower, upper = get_bollinger_band(bars, 20)
    #lower = []
    print(lower)

    for i in range(-8,0):
        c=last_candles[i]
        g=GenCandle(c.open, c.close,
               c.high, c.low,
               get_mMdistances(last_candles[i-20:i-1]),
               get_ocdistances(last_candles[i-20:i-1]),
               last_candles[i-1].close,
               upper[i]-lower[i],
               get_ema(last_candles[i-20:i-1], 18))
        addCandleToVector(g)

    determinePatterns()



if __name__ == '__main__':
    main()
