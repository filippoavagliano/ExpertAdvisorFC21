import MetaTrader5 as mt5
import pandas as pd


def mt5_connect():
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        quit()


def mt5_disconnect():
    mt5.shutdown()


def get_bars(symbol: str, timeframe: any, n: int) -> pd.DataFrame:
    """
    :param symbol:
    :param timeframe:
    :param n:
    :return: restituisce le ultime num_candles candele
    """
    mt5_connect()
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n)
    mt5_disconnect()
    return pd.DataFrame(rates)


if __name__ == '__main__':
    bar_df = get_bars("EURUSD", mt5.TIMEFRAME_H1, 10)
    print(bar_df)
