class Candle:
    def __init__(self, time: int, open, high, low, close):
        self.time = int(time)
        self.open = open
        self.high = high
        self.low = low
        self.close = close

    @classmethod
    def from_mt5_row(cls, row: tuple):
        """
        Inizializza la classe da una tupla restutita da MT5
        del tipo ('time', 'open', 'high', 'low', 'close', 'tick_volume', 'spread', 'real_volume')
        """
        data = row[1].tolist()
        return cls(data[0], data[1], data[2], data[3], data[4])

    @classmethod
    def from_pandas_row(cls, data):
        """
        Inizializza la classe da una tupla restutita da MT5
        del tipo ('time', 'open', 'high', 'low', 'close', 'tick_volume', 'spread', 'real_volume')
        """
        return cls(data[0], data[1], data[2], data[3], data[4])

    def get_shadow(self):
        return abs(self.high - self.low)

    def get_body(self):
        return abs(self.open - self.close)

    def __str__(self):
        return "time={}, open={}, close={}, high={}, low={}" \
            .format(self.time, self.open, self.close, self.high, self.low)
