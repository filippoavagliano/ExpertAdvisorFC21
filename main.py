import MetaTrader5 as mt5
import PatternDetector
import GenCandle
from mt5api import get_bars
from utils import get_ema, get_bollinger_band
from utilscandles import get_last_candles, extract_last_candles


def main():
    symbol = "EURUSD"
    timeframe = mt5.TIMEFRAME_H1
    num_of_candles = 29

    bars = get_bars(symbol, timeframe, num_of_candles)
    candles = extract_last_candles(bars, num_of_candles)

    last_candle = candles[-2]
    last_20_candles = candles[-20:-1]

    # bande di bollinger
    sma, lower, upper = get_bollinger_band(bars, 20)

    for i in range(-):
        with candles[i] as c:
    # GenCandle(c.open, c.close,
    #           c.high, c.low,
    #           get_mMdistances(last_20_candles),
    #           get_ocdistances(last_20_candles),
    #           None,
    #           get_ema(last_20_candles, 20))

    # TODO Codice da rivedere
    # for candle in candles:
    #     GenCandle.__init__(candle['open'], candle['close'], candle['max'], candle['min'])
    # PatternDetector.determinatePatterns(df)


if __name__ == '__main__':
    main()
