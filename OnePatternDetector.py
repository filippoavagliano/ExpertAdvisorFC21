class OnePatternDetector:

    @staticmethod
    def determinePattern(candleVector):

        vector = candleVector[-4:]
        type = vector[3].candleType

        if type == 12 or type == 13:
            if vector[3].EMAvalue <= vector[2].EMAvalue <= vector[1].EMAvalue <= vector[0].EMAvalue:
                vector[3].P.append(24)  # Hammer
                return

            if vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue:
                vector[3].P.append(25)  # Hanging man
                return

        if type == 5 and (vector[3].close <= vector[2].EMAvalue <= vector[1].EMAvalue <= vector[0].EMAvalue):
            vector[3].P.append(26)  # Bullish Belt Hold
            return

        if type == 4 and (vector[3].close >= vector[2].EMAvalue >= vector[1].EMAvalue >= vector[0].EMAvalue):
            vector[3].P.append(27)  # Bearish Belt Hold
            return

        vector[3].P.append(0)
        return
