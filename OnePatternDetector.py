class OnePatternDetector:

    def determinePattern(self, candleVector, type):

        vector=candleVector[-1:-4]

        if type==12 and type==13:
            if vector[3].EMAvalue <= vector[2].EMAvalue <= vector[1].EMAvalue <= vector[0].EMAvalue:
                vector[3].P.append(24)      # Hammer
                return

            if vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue:
                vector[3].P.append(25)      # Hanging man
                return

        if type == 5 and (vector[3].close <= vector[2].EMAvalue <= vector[1].EMAvalue <= vector[0].EMAvalue):
            vector[3].P.append(26)      # Bullish Belt Hold
            return

        if type == 4 and (vector[3].close >= vector[2].EMAvalue >= vector[1].EMAvalue >= vector[0].EMAvalue):
            vector[3].P.append(27)      # Bearish Belt Hold
            return

        vector[3].P.append(0)
        return