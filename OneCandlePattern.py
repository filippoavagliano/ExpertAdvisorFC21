class OneCandlePattern:

    def determinePattern(self, candleVector):

        vector=candleVector[-1:-4]

        if vector[0].EMAvalue == 0:
            return 0