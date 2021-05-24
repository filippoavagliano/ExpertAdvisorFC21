import MetaTrader5 as mt5
import PatternDetector
import GenCandle
from utils import get_ema
from utilscandles import get_last_candles


def main():
    symbol = "EURUSD"
    timeframe = mt5.TIMEFRAME_H1
    num_of_candles = 25

    candles = get_last_candles(num_of_candles, symbol, timeframe)

    last_candle = candles[-1]
    last_20_candles = candles[-20:-1]
    
    # GenCandle(c.open, c.close,
    #           c.high, c.low,
    #           get_mMdistances(last_20_candles),
    #           get_ocdistances(last_20_candles),
    #           None, # TODO Implementare metodo per calcolare bollBw
    #           get_ema(last_20_candles, 20))

    # TODO Codice da rivedere
    # for candle in candles:
    #     GenCandle.__init__(candle['open'], candle['close'], candle['max'], candle['min'])
    # PatternDetector.determinatePatterns(df)


if __name__ == '__main__':
    main()
