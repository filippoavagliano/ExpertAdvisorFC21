class OnePatternDetector:

    def determinePattern(self, candleVector):

        vector=candleVector[-1:-4]

        if ((vector[3].EMAvalue <= vector[2].EMAvalue <= vector[1].EMAvalue <= vector[0].EMAvalue)
                    and (vector[3].candleType == 12 or vector[3].candleType == 13)):
            vector[3].P.append(24)      # Hammer
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue)
                    and (vector[3].candleType == 12 or vector[3].candleType == 13)):
            vector[3].P.append(25)      # Hanging man
            return

        if ((vector[3].close <= vector[2].EMAvalue <= vector[1].EMAvalue <= vector[0].EMAvalue)
                    and vector[3].candleType == 5):
            vector[3].P.append(26)      # Bullish Belt Hold
            return

        if ((vector[3].close >= vector[2].EMAvalue >= vector[1].EMAvalue >= vector[0].EMAvalue)
                    and vector[3].candleType == 4):
            vector[3].P.append(27)      # Bearish Belt Hold
            return