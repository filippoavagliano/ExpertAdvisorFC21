import MetaTrader5 as mt5
from PatternDetector import addCandleToVector, determinePatterns
from GenCandle import GenCandle
from mt5api import get_bars
from utils import get_bollinger_band, calculate_ema
from utilscandles import extract_last_candles, get_ocdistances, get_mMdistances


def main():
    symbol = "EURUSD"
    timeframe = mt5.TIMEFRAME_H1
    num_of_candles = 100

    bars = get_bars(symbol, timeframe, num_of_candles)
    candles = extract_last_candles(bars, num_of_candles)

    bars = bars[:-1]
    last_candles = candles[:-1]

    print(bars)
    # bande di bollinger
    sma, lower, upper = get_bollinger_band(bars, 20)

    emas = calculate_ema(last_candles, 20)
    print(emas)

    for i in range(-8,0):
         c=last_candles[i]
         g=GenCandle(c.open, c.close,
                c.high, c.low,
                get_mMdistances(last_candles[i-20:i]),
                get_ocdistances(last_candles[i-20:i]),
                last_candles[i-1].close,
                ((upper[i]-lower[i])/sma[i])*100,
                emas[i])
         addCandleToVector(g)

    determinePatterns()



if __name__ == '__main__':
    main()
