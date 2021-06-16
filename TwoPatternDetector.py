import GenCandle


class TwoPatternDetector:

    @staticmethod
    def determinePattern(candleVector):

        vector = candleVector[-5:]
        type = vector[4].candleType



        if type == 1:

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue)
                    and vector[3].CBR <= 3 and vector[4].CBR >= 4 and vector[3].open < vector[4].close
                    and vector[3].close > vector[4].open and vector[3].open > vector[3].close and vector[4].open <
                    vector[4].close):
                vector[4].P.append(28)  # Bullish Engulfing
                return

            if ((vector[3].EMAvalue >= vector[2].EMAvalue >= vector[1].EMAvalue >= vector[0].EMAvalue)
                    and vector[3].CBR <= 3 and vector[4].CBR >= 4 and vector[3].open < vector[3].close
                    and vector[4].close > vector[4].open and vector[4].open > vector[3].close and vector[3].open >
                    vector[4].close):
                vector[4].P.append(29)  # Bearish Engulfing
                return

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue)
                    and vector[3].candleType == 1 and vector[3].open > vector[3].close and vector[4].open < vector[4].close
                    and vector[4].open < vector[3].minC and vector[4].close > vector[3].boc):
                vector[4].P.append(36)  # Piercing Line
                return

            if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue)
                    and vector[3].candleType == 1 and vector[3].open < vector[3].close and vector[4].open > vector[4].close
                    and vector[4].open > vector[3].minC and vector[4].close < vector[3].boc):
                vector[4].P.append(37)  # Red cloud cover
                return

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue)
                    and vector[3].candleType == 1 and vector[3].open > vector[3].close and vector[4].open < vector[4].close
                    and abs(vector[3].close - vector[4].close) <= 0.1 * min(vector[3].doc, vector[4].doc)):
                vector[4].P.append(40)  # Bullish Meeting Line
                return

            if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue)
                    and vector[3].candleType == 1 and vector[3].open < vector[3].close and vector[4].open > vector[4].close
                    and abs(vector[3].close - vector[4].close) <= 0.1 * min(vector[3].doc, vector[4].doc)):
                vector[4].P.append(41)  # Bearish Meeting Line
                return

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue)
                    and vector[3].candleType == 1 and vector[3].open > vector[3].close and vector[4].open < vector[4].close
                    and vector[4].open >= vector[3].close and vector[4].close > vector[3].maxC and vector[3].boc < vector[4].boc):
                vector[4].P.append(48)  # One Green Soldier
                return

            if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue)
                    and vector[3].candleType == 1 and vector[3].open < vector[3].close and vector[4].open > vector[4].close
                    and vector[4].open <= vector[3].close and vector[4].close < vector[3].minC and vector[3].boc > vector[4].boc):
                vector[4].P.append(49)  # One Red Crow
                return

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue) and vector[3].candleType == 1
                    and vector[3].open > vector[3].close
                    and vector[4].open < vector[4].close
                    and vector[4].open <= vector[3].minC
                    and abs(vector[3].close - vector[4].open) > 2 * abs(vector[3].close - vector[3].minC)
                    and abs(vector[4].close - vector[3].close) > 2 * abs(vector[3].close - vector[3].minC)
                    and vector[4].boc < vector[3].boc): #far controllare
                vector[4].P.append[96]  # Bearish Thrusting lines
                return

            if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue) and vector[3].candleType == 1
                    and vector[3].open < vector[3].close
                    and vector[4].open > vector[4].close
                    and vector[4].open >= vector[3].maxC
                    and abs(vector[4].close - vector[4].open) > 2 * abs(vector[3].close - vector[3].maxC)
                    and abs(vector[4].close - vector[3].close) > 2 * abs(vector[3].close - vector[3].maxC)
                    and vector[4].boc < vector[3].boc): #far controllare
                vector[4].P.append[97]  # Bullish Thrusting lines
                return


        if (type == 2):

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue)
                    and vector[3].candleType == 1 and vector[3].open > vector[3].close and vector[4].open > vector[4].close
                    and vector[3].close < vector[4].open < vector[3].open and vector[3].close < vector[4].close < vector[3].open
                    and (vector[4].maxC < vector[3].open or None) and (vector[4].minC > vector[3].close or None)):
                vector[4].P.append[42]  # Homing Pigeon
                return

            if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue)
                    and vector[3].candleType == 1 and vector[3].open < vector[3].close and vector[4].open < vector[4].close
                    and vector[3].open < vector[4].open < vector[3].close and vector[3].open < vector[4].close < vector[3].close):
                vector[4].P.append[43]  # Descending Hawk
                return

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                    and vector[3].candleType == 1 and vector[3].open > vector[3].close and vector[4].open > vector[4].close
                    and vector[3].close < vector[4].open < vector[3].open and abs(vector[3].close - vector[4].close) <= 0.1 * vector[4].doc
                    and vector[3].doc > vector[4].doc and abs(vector[3].close - vector[3].minC) <= 0.15 * vector[3].dmM
                    and abs(vector[4].close - vector[4].minC) <= 0.15 * vector[4].dmM):
                # opzionali M(t) < o(t-1) e m(t) > c(t-1)
                vector[4].P.append[44]  # Matching Low
                return

            if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                    and vector[3].candleType == 1 and vector[3].open < vector[3].close and vector[4].open < vector[4].close
                    and vector[3].open < vector[4].open < vector[3].close and abs(vector[3].close - vector[4].close) <= 0.1 * vector[4].doc
                    and vector[3].doc > vector[4].doc and abs(vector[3].close - vector[3].maxC) <= 0.15 * vector[3].dmM
                    and abs(vector[4].close - vector[4].maxC) <= 0.15 * vector[4].dmM):
                # opzionali M(t) < o(t-1) e m(t) > c(t-1)
                vector[4].P.append[45]  # Matching High
                return

        if (vector[4].CBR >=2):

            if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue) and vector[3].CBR >= 2 and vector[3].open > vector[3].close
                    and vector[4].open < vector[4].close
                    and abs(vector[3].open - vector[4].open) <= 0.1 * ((vector[3].doc + vector[4].doc)/2)
                    and vector[4].boc > vector[3].boc):
                vector[4].P.append[90]  # Bullish Separating lines
                return

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue) and vector[3].CBR >= 2 and vector[3].open < vector[3].close
                    and vector[4].open > vector[4].close
                    and abs(vector[3].open - vector[4].open) <= 0.1 * ((vector[3].doc + vector[4].doc)/2)
                    and vector[4].boc < vector[3].boc):
                vector[4].P.append[91]  # Bearish Separating lines
                return

        if (type == 2):

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue) and vector[3].candleType == 1
                    and vector[3].open > vector[3].close
                    and vector[4].open < vector[4].close
                    and vector[4].open <= vector[3].close
                    and abs(vector[4].close - vector[3].minC) <= 0.1 * ((vector[3].doc + vector[4].doc)/2)
                    and vector[4].boc < vector[3].boc):
                vector[4].P.append[92]  # Bearish One Neck lines
                return

            if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue) and vector[3].candleType == 1
                    and vector[3].open < vector[3].close
                    and vector[4].open > vector[4].close
                    and vector[4].open > vector[3].close
                    and abs(vector[4].close - vector[3].maxC) <= 0.1 * ((vector[3].doc + vector[4].doc)/2)
                    and vector[4].boc > vector[3].boc):
                vector[4].P.append[93]  # Bullish One Neck lines
                return

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue) and vector[3].candleType == 1
                    and vector[3].open > vector[3].close
                    and vector[4].open < vector[4].close
                    and vector[4].open <= vector[3].close
                    and vector[4].close >= vector[3].close
                    and vector[4].dmM < vector[3].dmM
                    and vector[4].boc < vector[3].boc):
                vector[4].P.append[94]  # Bearish In Neck lines
                return

            if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue) and vector[3].candleType == 1
                    and vector[3].open < vector[3].close
                    and vector[4].open > vector[4].close
                    and vector[4].open >= vector[3].close
                    and vector[4].close <= vector[3].close
                    and vector[4].dmM < vector[3].dmM
                    and vector[4].boc > vector[3].boc):
                vector[4].P.append[94]  # Bullish In Neck lines
                return

        if 2 <= vector[4].CBR <= 3:

            if ((vector[4].CBR >= 2 and vector[4].CBR <= 3) and vector[3].CBR >= 4
                    and vector[4].mb > vector[3].close and vector[3].open < vector[3].close):
                vector[4].P.append(18)  # Bullish Star
                return

            if ((vector[4].CBR >= 2 and vector[4].CBR <= 3) and vector[3].CBR >= 4
                    and vector[4].Mb < vector[3].close and vector[3].open > vector[3].close):
                vector[4].P.append(19)  # Bearish Star
                return

        if vector[4].CBR <= 3:

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue)
                    and vector[3].CBR >= 4 and vector[4].CBR <= 3 and vector[3].open > vector[4].close and vector[3].close < vector[4].open
                    and vector[3].open > vector[3].close and vector[4].open < vector[4].close):
                vector[4].P.append(30)  # Bullish Harami
                return

            if ((vector[3].EMAvalue >= vector[2].EMAvalue >= vector[1].EMAvalue >= vector[0].EMAvalue)
                    and vector[3].CBR >= 4 and vector[4].CBR <= 3 and vector[3].open < vector[4].close and vector[3].close > vector[4].open
                    and vector[3].open < vector[3].close and vector[4].open > vector[4].close):
                vector[4].P.append(31)  # Bearish Harami
                return

        if type == 7:

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                    and vector[3].CBR >= 4 and vector[4].candleType == 7 and vector[4].dmM < vector[3].doc and
                    vector[3].open > vector[3].close):
                vector[4].P.append(32)  # Bullish Cross Harami
                return

            if ((vector[4].EMAvalue >= vector[3].EMAvalue >= vector[2].EMAvalue >= vector[1].EMAvalue >= vector[0].EMAvalue)
                    and vector[3].CBR >= 4 and vector[4].candleType == 7 and vector[4].dmM < vector[3].doc and
                    vector[3].open < vector[3].close):
                vector[4].P.append(33)  # Bearish Cross Harami
                return

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                    and vector[3].CBR >= 4 and vector[3].open > vector[3].close and vector[4].open < vector[3].close):
                vector[4].P.append(32)  # Bullish Doji Star
                return

            if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                    and vector[3].CBR >= 4 and vector[3].open < vector[3].close and vector[4].open > vector[3].close):
                vector[4].P.append(32)  # Bearish Doji Star
                return

        if type == 14 or type == 15:

            if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                    and (vector[4].candleType == 14 or vector[4].candleType == 15) and vector[4].CBR >= 1 and
                    vector[4].CBR <= 3
                    and vector[4].boc < vector[4].bmM and vector[4].S <= -1 and (
                            (vector[4].mb - 0.1 * vector[4].doc) <= vector[4].minC <= vector[4].Mb)
                    and vector[3].doc > vector[4].doc and vector[3].CBR >= 2 and vector[3].CBR <= 4 and vector[4].Mb < vector[3].close):
                vector[4].P.append(34)  # Inverted Hammer
                return

            if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                    and (vector[4].candleType == 14 or vector[4].candleType == 15) and vector[4].CBR >= 1 and
                    vector[4].CBR <= 3
                    and vector[4].boc < vector[4].bmM and vector[4].S <= -1 and (
                            (vector[4].mb - 0.1 * vector[4].doc) <= vector[4].minC <= vector[4].Mb)
                    and vector[3].doc < vector[4].doc and vector[3].CBR >= 2 and vector[3].CBR <= 4 and vector[4].Mb > vector[3].close):
                vector[4].P.append(34)  # Shooting Star
                return

        if type == 3 or type == 4 or type == 5:

            if (vector[3].candleType == 3 and vector[3].open > vector[3].close and vector[4].open < vector[4].close
                    and vector[3].open < vector[4].open and vector[3].doc < vector[4].doc):
                vector[4].P.append(46)  # Bullish Kicking
                return

            if (vector[3].candleType == 3 and vector[3].open > vector[3].close and vector[4].open < vector[4].close
                    and vector[3].open < vector[4].open and vector[3].doc < vector[4].doc):
                vector[4].P.append(46)  # Bearish Kicking
                return


        vector[4].P.append(0)
        return
