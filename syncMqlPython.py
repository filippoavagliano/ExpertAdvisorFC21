import MetaTrader5 as mt5
import pandas as pd


def mt5_connect():
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        quit()


def mt5_disconnect():
    mt5.shutdown()


def get_last_candles(symbol: str, timeframe: any, num_candles: int) -> pd.DataFrame:
    """
    :param symbol:
    :param timeframe:
    :param num_candles:
    :return: restituisce le ultime num_candles candele
    """
    mt5_connect()
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 1, num_candles)
    mt5_disconnect()
    return pd.DataFrame(rates)


def main():
    symbol = "EURUSD"
    timeframe = mt5.TIMEFRAME_H1
    num_of_candles = 8

    df = get_last_candles(symbol, timeframe, num_of_candles)

    print("Stampo le ultime {} candele".format(num_of_candles))
    print(df)

    open = df['open'][0]
    close = df['close'][0]

    print("open:", open, "close:", close, "diff:", open - close)


if __name__ == '__main__':
    main()
