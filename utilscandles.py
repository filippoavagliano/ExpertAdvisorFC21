from typing import List

import pandas

from Candle import Candle

from mt5api import get_bars


def get_mMdistances(candles: List[Candle]):
    """
    Restituisce una lista con le ombre delle candele passate in input
    :param candles (Candle[])
    """
    return [c.get_shadow() for c in candles]


def get_ocdistances(candles: List[Candle]):
    """
    Restituisce una lista con i body delle candele passate in input
    :param candles (Candle[])
    """

    return [c.get_body() for c in candles]



def extract_last_candles(df: pandas.DataFrame, n: int) -> List[Candle]:
    """
    Restituisce una lista di Candle.
    La candela più recente è in ultima posizione.
    :param df: Dataframe da cui le candele sono estratte
    :param n: numero di candele da estrarre
    """
    # [Candle.from_pandas_row(df.iloc[-i]) for i in range(1, n + 1)] # reverse order
    return [Candle.from_pandas_row(df.iloc[i]) for i in range(n)]


def get_last_candles(n: int, symbol: str, timeframe: any) -> List[Candle]:
    """
    Restituisce una lista di Candle richiamando direttamente MetaTrader 5.
    La candela più recente è in ultima posizione.
    :param n: numero di candele da restituire
    :param symbol:
    :param timeframe:
    :return:
    """
    df = get_bars(symbol, timeframe, n)
    # [Candle.from_pandas_row(df.iloc[-i]) for i in range(1, n + 1)] # reverse order
    return [Candle.from_pandas_row(df.iloc[i]) for i in range(n)]
