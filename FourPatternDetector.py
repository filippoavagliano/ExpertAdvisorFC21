class FourPatternDetector:

    @staticmethod
    def determinePattern(candleVector):

        vector = candleVector[-1:-7]
        type = vector[6].candleType


        if (vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue <= vector[5].EMAvalue <= vector[6].EMAvalue
            and vector[3].candleType == 4 and vector[4].candleType == 4 and vector[5].open > vector[4].close
            and vector[5].maxC > vector[4].close and vector[5].boc < vector[5].bmM and vector[6].maxC > vector[5].maxC
            and vector[6].minC < vector[5].minC and vector[6].bmM > vector[5].bmM):

            vector[6].P.append(83)              #Concealing Baby Shallow

        if (vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue >= vector[5].EMAvalue >= vector[6].EMAvalue
            and (min(vector[3].open, vector[3].close) > max(vector[4].open, vector[4].close))
            and min(vector[4].open, vector[4].close) > vector[5].open
            and vector[5].open > vector[5].close and vector[5].close > vector[6].open and vector[6].open > vector[6].close
            and vector[3].minC > vector[4].minC > vector[5].minC > vector[6].micC
            and vector[3].maxC > vector[4].maxC > vector[5].maxC > vector[6].maxC
            and vector[5].CBR >= 2 and vector[6].CBR >= 2
            and abs(min(vector[3].open),vector[3].close - max(vector[4].open, vector[4].close)) > 0.1 * vector[3].dmM
            and abs( min(vector[4].open, vector[4].close) - vector[5].open) > 0.1 * vector[4].dmM
            and abs( vector[5].close - vector[6].open) > 0.1 * vector[5].dmM):
            vector[6].P.append(88)              #Three Gaps Down

        if (vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue <= vector[5].EMAvalue <= vector[6].EMAvalue
            and (max(vector[3].open, vector[3].close) < min(vector[4].open, vector[4].close))
            and max(vector[4].open, vector[4].close) < vector[5].open
            and vector[5].open < vector[5].close and vector[5].close < vector[6].open
            and vector[6].open < vector[6].close
            and vector[3].minC < vector[4].minC < vector[5].minC < vector[6].micC
            and vector[3].maxC < vector[4].maxC < vector[5].maxC < vector[6].maxC
            and vector[5].CBR >= 2 and vector[6].CBR >= 2
            and abs(max(vector[3].open), vector[3].close - min(vector[4].open, vector[4].close)) > 0.1 * vector[3].dmM
            and abs(max(vector[4].open, vector[4].close) - vector[5].open) > 0.1 * vector[4].dmM
            and abs(vector[5].close - vector[6].open) > 0.1 * vector[5].dmM):
            vector[6].P.append(89)  # Three Gaps Up



# Patterns di continuazione

        if (vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue <= vector[5].EMAvalue <= vector[6].EMAvalue
            and vector[2].open < vector[2].close and vector[3].open < vector[3].close
            and vector[4].open < vector[4].close and vector[6].close >= max(vector[3].close, vector[4].close, vector[5].close)
            and vector[6].close < vector[2].minC):
            vector[6].P.append(111)         #Three- line strike rialzista

        if (vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue >= vector[5].EMAvalue >= vector[6].EMAvalue
            and vector[2].open > vector[2].close and vector[3].open > vector[3].close and vector[4].open > vector[4].close
            and vector[6].open <= min(vector[3].close, vector[4].close, vector[5].close)
            and vector[6].close > vector[2].maxC):
            vector.P.append(112)            #Three line strike bearish







