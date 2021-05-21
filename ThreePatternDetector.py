class ThreePatternDetector:

    @staticmethod
    def determinePattern(candleVector):

        vector = candleVector[-1:-6]
        type = vector[5].candleType

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
            and vector[3].candleType == 1 and vector[5].CBR >= 2 and vector[3].open > vector[3].close > vector[4].Mb
            < (vector[5].open or None) and vector[5].open < vector[5].close > vector[3].boc):
                vector[5].P.append(50)          # Morning Star
                return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
            and vector[3].candleType == 1 and vector[5].CBR >= 2 and vector[3].open < vector[3].close < vector[4].mb
            > (vector[5].open or None) and vector[5].open > vector[5].close < vector[3].boc):
                vector[5].P.append(51)          # Evening Star
                return

        if (vector[4].P[1] == 38 and vector[5].CBR >= 2 and vector[3].open > vector[3].close and vector[3].boc <= vector[5].close
            > vector[5].open >= (vector[4].Mb or None)):

            if vector[4].maxC < vector[3].minC and vector[4].maxC < vector[5].minC:
                vector[5].P.append(54)      # Bullish Abandoned Baby
                return

            vector[5].P.append(52)          # Morning Doji Star
            return

        if (vector[4].P[1] == 39 and vector[5].CBR >= 2 and vector[3].open < vector[3].close and vector[3].boc >= vector[5].close
            < vector[5].open <= (vector[4].mb or None)):

            if vector[4].maxC < vector[3].minC and vector[4].maxC < vector[5].minC:
                vector[5].P.append(55)      # Bearish Abandoned Baby
                return

            vector[5].P.append(53)          # Evening Doji Star
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
            and vector[5].candleType == vector[4].candleType == vector[3].candleType == 7 and vector[4].bmM < vector[3].bmM
            and vector[4].bmM < vector[5].bmM):

            vector[5].P.append(56)          # Bullish Tri Star
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
            and vector[5].candleType == vector[4].candleType == vector[3].candleType == 7 and vector[4].bmM > vector[3].bmM
            and vector[4].bmM > vector[5].bmM):

            vector[5].P.append(57)          # Bearish Tri Star
            return