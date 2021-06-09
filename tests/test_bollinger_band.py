import MetaTrader5 as mt5

from mt5api import get_bars
from utils import get_bollinger_band, plot_bollinger_band


def main():
    symbol = "EURUSD"
    timeframe = mt5.TIMEFRAME_D1
    num_of_candles = 40

    bars = get_bars(symbol, timeframe, num_of_candles)
    bb = get_bollinger_band(bars, 20)
    plot_bollinger_band(bars['close'].to_list(), *bb)



if __name__ == '__main__':
    main()
