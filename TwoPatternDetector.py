class TwoPatternDetector:

    def determinePattern(self, candleVector):

        vector = candleVector[-1:-5]

        if ((vector[4].CBR >=2 and vector[4].CBR <= 3) and vector[3].CBR >= 4
                    and vector[4].mb > vector[3].close and vector[3].open < vector[3].close):
            vector[4].P.append(18)      # Bullish Star
            return

        if ((vector[4].CBR >=2 and vector[4].CBR <= 3) and vector[3].CBR >= 4
                    and vector[4].Mb < vector[3].close and vector[3].open > vector[3].close):
            vector[4].P.append(19)      # Bearish Star
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                    and vector[3].CBR <=3 and vector[4] >= 4 and vector[3].open < vector[4].close
                    and vector[3].close > vector[4].open and vector[3].open > vector[3].close and vector[4].open < vector[4].close):
            vector[4].P.append(28)        # Bullish Engulfing
            return

        if ((vector[4].EMAvalue >= vector[3].EMAvalue >= vector[2].EMAvalue >= vector[1].EMAvalue >= vector[0].EMAvalue)
                    and vector[3].CBR <=3 and vector[4] >= 4 and vector[3].open < vector[3].close
                    and vector[4].close > vector[4].open and vector[4].open > vector[3].close and vector[3].open > vector[4].close):
            vector[4].P.append(29)        # Bearish Engulfing
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                    and vector[3].CBR >= 4 and vector[4].CBR <= 3 and vector[3].open > vector[4].close and vector[3].close < vector[4].open
                    and vector[3].open > vector[3].close and vector[4].open < vector[4].close):
            vector[4].P.append(30)        # Bullish Harami
            return

        if ((vector[4].EMAvalue >= vector[3].EMAvalue >= vector[2].EMAvalue >= vector[1].EMAvalue >= vector[0].EMAvalue)
                    and vector[3].CBR >= 4 and vector[4].CBR <= 3 and vector[3].open < vector[4].close and vector[3].close > vector[4].open
                    and vector[3].open < vector[3].close and vector[4].open > vector[4].close):
            vector[4].P.append(31)        # Bearish Harami
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                    and vector[3].CBR >= 4 and vector[4].candleType==7 and vector[4].dmM < vector[3].doc and vector[3].open > vector[3].close):
            vector[4].P.append(32)        # Bullish Cross Harami
            return

        if ((vector[4].EMAvalue >= vector[3].EMAvalue >= vector[2].EMAvalue >= vector[1].EMAvalue >= vector[0].EMAvalue)
                    and vector[3].CBR >= 4 and vector[4].candleType==7 and vector[4].dmM < vector[3].doc and vector[3].open < vector[3].close):
            vector[4].P.append(33)        # Bearish Cross Harami
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                    and (vector[4].candleType==14 or vector[4].candleType==15) and vector[4].CBR >= 1 and vector[4].CBR <= 3
                    and vector[4].boc < vector[4].bmM and vector[4].S <= -1 and ((vector[4].mb - 0.1*vector[4].doc) <= vector[4].minC <= vector[4].Mb)
                    and vector[3].doc > vector[4].doc and vector[4].CBR >= 2 and vector[4].CBR <= 4 and vector[4].Mb < vector[3].close):
            vector[4].P.append(34)        # Inverted Hammer
            return





