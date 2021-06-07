class FivePatternDetector:

    @staticmethod
    def determinePattern(vector):

        type = vector[7].candleType

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue >= vector[5].EMAvalue >= vector[6].EMAvalue >= vector[7].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open > vector[3].close and vector[4].open > vector[4].close and vector[4].open < vector[3].minC and vector[4].close > min(vector[5].open, vector[5].close) > vector[6].close
                and (vector[7].open < vector[5].close or None) and vector[7].open < vector[7].close and vector[7].close > vector[4].open and vector[6].open < vector[7].close
                and vector[7].CBR >= 3):
            vector[7].P.append(81)          # Bullish Breakaway
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue <= vector[5].EMAvalue <= vector[6].EMAvalue <= vector[7].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open < vector[3].close and vector[4].open < vector[4].close and vector[4].open > vector[3].maxC and vector[4].close < max(vector[5].open, vector[5].close) < vector[6].close
                and (vector[5].open > vector[5].close or None) and vector[7].open > vector[7].close and vector[7].close < vector[6].open and vector[7].close < vector[4].open
                and vector[7].CBR >= 3):
            vector[7].P.append(82)          # Bearish Breakaway
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue >= vector[5].EMAvalue >= vector[6].EMAvalue)
                and vector[3].close < vector[3].open and vector[4].close < vector[4].open and vector[5].close < vector[5].open and vector[6].close < vector[6].open
                and vector[7].close > vector[7].open and vector[6].maxC > vector[5].boc and vector[3].maxC > vector[4].maxC > vector[5].maxC
                and vector[3].minC > vector[4].minC > vector[5].minC > vector[6].minC and vector[6].boc < vector[7].open and vector[6].boc < vector[6].bmM
                and vector[7].close > vector[6].maxC):
            vector[7].P.append(84)          # Ladder Bottom
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue <= vector[5].EMAvalue <= vector[6].EMAvalue)
                and vector[3].close > vector[3].open and vector[4].close > vector[4].open and vector[5].close > vector[5].open and vector[6].close > vector[6].open
                and vector[7].close < vector[7].open and vector[6].minC < vector[5].boc and vector[3].maxC < vector[4].maxC < vector[5].maxC < vector[6].maxC
                and vector[3].minC < vector[4].minC < vector[5].minC and vector[6].boc > vector[7].open and vector[6].boc > vector[6].bmM
                and vector[7].close < vector[6].minC):
            vector[7].P.append(85)          # Ladder Top
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue >= vector[5].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open > vector[3].close and vector[4].open > vector[4].close and vector[5].open > vector[5].close
                and vector[6].open < vector[6].close
                and vector[5].open < vector[4].close and vector[7].open < vector[7].close and vector[7].open > vector[6].close
                and vector[3].maxC > vector[4].maxC > vector[5].maxC and vector[5].maxC < vector[6].maxC < vector[7].maxC and vector[3].minC > vector[4].minC > vector[5].minC
                and vector[5].minC < vector[6].minC < vector[7].minC):
            vector[7].P.append(86)          # After Bottom Gap Up
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue <= vector[5].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open < vector[3].close and vector[4].open < vector[4].close and vector[5].open < vector[5].close
                and vector[6].open > vector[6].close
                and vector[5].open > vector[4].close and vector[7].open > vector[7].close and vector[7].open < vector[6].close
                and vector[3].maxC < vector[4].maxC < vector[5].maxC and vector[5].maxC > vector[6].maxC > vector[7].maxC and vector[3].minC < vector[4].minC < vector[5].minC
                and vector[5].minC > vector[6].minC > vector[7].minC):
            vector[7].P.append(87)          # After Top Gap Down
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open < vector[3].close and vector[4].dmM < vector[3].dmM and vector[5].dmM < vector[3].dmM and vector[6].dmM < vector[3].dmM
                and vector[3].maxC > vector[4].maxC and vector[3].maxC > vector[5].maxC and vector[3].maxC > vector[6].maxC and vector[3].minC < vector[4].minC and vector[3].minC < vector[5].minC and vector[3].minC < vector[6].minC
                and vector[7].open > vector[3].minC and vector[7].close > vector[3].maxC and vector[7].open < vector[7].close and (vector[7].candleType == 1 or None) and vector[7].boc > vector[3].boc
                and (vector[4].open > vector[4].close or None) and (vector[5].open > vector[5].close or None) and (vector[6].open > vector[6].close or None)):
            vector[7].P.append(107)          # Rising three metod
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open > vector[3].close and vector[3].dmM > vector[4].dmM and vector[3].dmM > vector[5].dmM and vector[3].dmM > vector[6].dmM
                and vector[3].maxC > vector[4].maxC and vector[3].maxC > vector[5].maxC and vector[3].maxC > vector[6].maxC and vector[3].minC < vector[4].minC and vector[3].minC < vector[5].minC and vector[3].minC < vector[6].minC
                and vector[7].open < vector[3].maxC and vector[7].close < vector[3].minC and vector[7].open > vector[7].close and (vector[7].candleType == 1 or None) and vector[7].boc < vector[3].boc
                and (vector[4].open < vector[4].close or None) and (vector[5].open < vector[5].close or None) and (vector[6].open < vector[6].close or None)):
            vector[7].P.append(108)          # Falling three metod
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open < vector[3].close and vector[4].open > vector[4].close and vector[4].open > vector[3].close and vector[6].open > vector[6].close
                and vector[6].open < vector[3].close and vector[7].open < vector[7].close and vector[7].maxC > vector[3].maxC and vector[3].boc < vector[7].boc and ((vector[4].maxC > vector[5].maxC > vector[6].maxC) or None)
                and ((vector[4].minC > vector[5].minC > vector[6].minC) or None)):
            vector[7].P.append(109)          # Bullish Mat Hold
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open > vector[3].close and vector[4].open < vector[4].close and vector[4].open < vector[3].close and vector[6].open < vector[6].close
                and vector[6].open > vector[3].close and vector[7].open > vector[7].close and vector[7].minC > vector[3].minC and vector[3].boc > vector[7].boc and ((vector[4].maxC < vector[5].maxC < vector[6].maxC) or None)
                and ((vector[4].minC < vector[5].minC < vector[6].minC) or None)):
            vector[7].P.append(109)          # Bearish Mat Hold
            return
