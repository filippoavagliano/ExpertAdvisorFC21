class ThreePatternDetector:

    @staticmethod
    def determinePattern(candleVector):

        vector = candleVector[-6:]
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

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                and vector[3].CBR >= 4 and vector[3].open < vector[3].close and vector[4].close > vector[3].close
                and vector[5].open > vector[4].open and vector[5].close < vector[4].close and vector[5].open >= vector[4].maxC
                and vector[5].close <= vector[4].minC and vector[5].close > vector[3].close):

            vector[5].P.append(58)          # Upside gap two crow
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                and vector[3].CBR >= 4 and vector[3].open > vector[3].close and vector[4].close < vector[3].close
                and vector[5].open < vector[4].open and vector[5].close > vector[4].close and vector[5].open <= vector[4].minC
                and vector[5].close >= vector[4].maxC and vector[5].close < vector[3].close):
            vector[5].P.append(59)          # Downside gap two rabbits
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                and vector[3].CBR >= 4 and vector[3].open > vector[3].close and vector[3].doc > vector[4].doc and vector[3].open > vector[4].close
                and vector[3].close < vector[4].close and vector[3].mb > vector[4].mb and vector[4].CBR <= 2 and vector[5].CBR >= 2  #short range o long range opzionale
                and vector[5].open < vector[5].close and vector[5].boc < vector[4].boc):
            vector[5].P.append(60)          # Unique three rives bottom
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                and vector[3].CBR >= 4 and vector[3].open < vector[3].close and vector[3].doc > vector[4].doc and vector[3].open < vector[4].open
                and vector[3].close > vector[4].close and vector[3].Mb > vector[4].Mb and vector[4].CBR <= 2 and vector[5].CBR >= 2
                and vector[5].open > vector[5].close and vector[5].boc > vector[4].boc):
            vector[5].P.append(61)          # Unique three mountain top
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                and vector[3].CBR >= 4 and vector[4].CBR >= 4 and vector[5].CBR >= 4 and vector[3].open < vector[3].close and vector[4].open < vector[4].close
                and vector[5].open < vector[5].close and (vector[3].close < vector[4].close < vector[5].close)
                and (vector[2].open < vector[4].open < vector[5].open) and (vector[4].open < vector[5].open < vector[4].close)):
            vector[5].P.append(62)          # Three green soldier
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue)
                and vector[3].CBR >= 4 and vector[4].CBR >= 4 and vector[5] >= 4 and vector[3].open > vector[3].close
                and vector[4].open > vector[4].close and vector[5].open > vector[5].close and (vector[3].close > vector[4].close > vector[5].close)
                and (vector[3].close < vector[4].open < vector[3].open) and (vector[4].close < vector[5].open < vector[4].open)):
            vector[5].P.append(63)          # three red crows
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue)
                and vector[3].CBR >= 4 and vector[4].CBR >= 4 and vector[5].CBR >= 4 and vector[3].open > vector[3].close
                and vector[4].open > vector[4].close and vector[5].open > vector[5].close and (vector[3].close > vector[4].close > vector[5].close)
                and (abs(vector[3].close-vector[4].open) <= 0.1 * ((vector[3].doc+vector[4].doc+vector[5].doc)/3))
                and (abs(vector[4].close-vector[5].open) <= 0.1 * ((vector[3].doc+vector[4].doc+vector[5].doc)/3)) ):
            vector[5].P.append(64)          #Identical three crows
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue <= vector[5].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open < vector[3].close and vector[4].open < vector[4].close and vector[5] < vector[5].close
                and (vector[3].boc < vector[4].boc < vector[4].bmM) and vector[4].CBR <= 3 and ((vector[4].boc < vector[5].boc < vector[5].bmM) or None )
                and (vector[5].close > vector[4].close > vector[3].close) and (vector[3].open < vector[4].open < vector[3].close)
                and (vector[4].open < vector[5].open < vector[4].close)):
            vector[5].P.append(65)          #Advance Black
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue >= vector[5].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open > vector[3].close and vector[4].open > vector[4].close and vector[5].open > vector[5].close
                and (vector[3].close > vector[4].close > vector[5].close) and vector[4].CBR <= 3 and vector[5].CBR <= 3
                and ((vector[5].doc / vector[5].dmM) < (vector[4].doc / vector[4].dmM)) and (vector[3].close < vector[4].open < vector[3].open)
                and (vector[4].close < vector[5].open < vector[4].open) and (vector[3].boc < vector[4].boc < vector[4].bmM)
                and (vector[4].boc < vector[5].boc < vector[5].bmM)):
            vector[5].P.append(66)          #Descent block
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue <= vector[5].EMAvalue)
                and vector[3].candleType == 1 and vector[4].candleType == 1 and vector[3].open < vector[3].close and vector[4].open < vector[4].close
                and vector[5].open < vector[5].close and vector[5].CBR <= 3
                and abs(vector[5].open - vector[4].close) <= 0.1 * ((vector[3].boc + vector[4].boc + vector[5].boc) / 3)):
            vector[5].P.append(67)          # Bearish deliberation
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue >= vector[5].EMAvalue)
                and vector[3].candleType == 1 and vector[4].candleType == 1 and (2 < vector[5].CBR < 3)
                and abs(vector[5].open - vector[4].close) <= 0.1 * ((vector[3].boc + vector[4].boc + vector[5].boc) / 3)
                and vector[3].open > vector[3].close and vector[4].open > vector[4].close
                and vector[5].open > vector[5].close):
            vector[5].P.append(68)          # Bullish deliberation
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open < vector[3].close and vector[4].open > vector[4].close
                and vector[5].open > vector[5].close and vector[5].open <= vector[4].boc and vector[4].close > vector[3].close
                and vector[5].close < vector[3].close and vector[5].boc < vector[4].boc):
            vector[5].P.append(69)          # Two Crows
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                and vector[3].candleType == 1 and vector[3].open > vector[3].close and vector[4].open < vector[4].close
                and vector[5].open < vector[5].close and vector[5].open >= vector[4].boc and vector[4].close < vector[3].close
                and vector[5].close > vector[3].close and vector[5].boc > vector[4].boc):
            vector[5].P.append(70)          # Two Rabbits
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                and (vector[4].P[1] == 30 or 32) and (vector[5].open < vector[5].close > vector[3].Mb) and vector[3].boc < vector[5].boc > vector[4].boc):
            vector[5].P.append(71)          # Three inside up
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                and (vector[4].P[1] == 31 or 33) and (vector[5].open > vector[5].close < vector[3].mb) and (vector[3].boc > vector[5].boc < vector[4].boc)):
            vector[5].P.append(72)          # Three inside down
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                and (vector[4].P[1] == 28) and vector[5].open < vector[5].close and vector[5].close > vector[4].Mb
                and vector[4].boc < vector[5].boc):
            vector[5].P.append(73)          # Three outside up
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                and (vector[4].P[1] == 29) and vector[5].open > vector[5].close and vector[5].close < vector[4].mb
                and vector[4].boc > vector[5].boc):
            vector[5].P.append(74)          # Three outside down
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                and vector[3].CBR >= 2 and vector[3].open > vector[3].close and vector[3].boc > vector[3].bmM
                and (abs(vector[3].open - vector[3].maxC) <=  0.2 * vector[3].dmM) and vector[4].CBR >=2
                and vector[4].open > vector[4].close and vector[4].boc > vector[4].bmM
                and (abs(vector[4].open - vector[4].maxC) <=  0.2 * vector[4].dmM)
                and vector[3].minC < vector[4].minC < vector[5].minC
                and vector[3].maxC > vector[4].maxC > vector[5].maxC
                and vector[5].candleType == 5 and (vector[4].minC < vector[5].minC < vector[5].maxC < vector[4].maxC)):
            vector[5].P.append(75)          # Three stars in the south
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                and vector[3].CBR >= 2 and vector[3].open < vector[3].close and vector[3].boc < vector[3].bmM
                and (abs(vector[3].open - vector[3].minC) <= 0.2 * vector[3].dmM) and vector[4].CBR >= 2
                and vector[4].open < vector[4].close and vector[4].boc < vector[4].bmM
                and (abs(vector[4].open - vector[4].minC) <= 0.2 * vector[4].dmM)
                and vector[3].minC < vector[4].minC < vector[5].minC
                and vector[3].maxC > vector[4].maxC > vector[5].maxC
                and vector[5].candleType == 4 and (vector[4].minC < vector[5].minC < vector[5].maxC < vector[4].maxC)):
            vector[5].P.append(76)          # Three stars in the north
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue)
                and (vector[3].candleType == 5 or 1) and vector[3].close < vector[3].open  and (vector[4].candleType == 1 or 3)
                and vector[4].open < vector[4].close and (vector[5].candleType == 5 or 1)
                and vector[5].close < vector[5].open and abs(vector[3].minC - vector[5].minC) <= 0.1 * ((vector[3].boc + vector[4].boc + vector[5].boc) / 3)
                and vector[4].boc > vector[3].boc and vector[4].close > vector[3].open and vector[5].open>vector[4].close):
            vector[5].P.append(77)          # Bullish Stick sandwich
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue)
                and (vector[3].candleType == 4 or 1) and vector[3].close > vector[3].open and (vector[4].candleType == 1 or 3)
                and vector[4].open > vector[4].close and (vector[5].candleType == 5 or 1)
                and vector[5].close > vector[5].open and abs(vector[3].maxC - vector[5].maxC) <= 0.1 * ((vector[3].boc + vector[4].boc + vector[5].boc) / 3)
                and vector[4].boc < vector[3].boc and vector[4].close < vector[3].open and vector[5].open < vector[4].close):
            vector[5].P.append(78)          # Bearish Stick sandwich
            return

        if ( ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue) or None)
                and (vector[2].candleType == 1 or 2) and vector[2].open > vector[2].close
                and vector[2].minC < (max(vector[3].open,vector[3].close)) < vector[2].maxC
                and vector[3].minC < max(vector[4].open, vector[4].close) < vector[3].maxC
                and vector[2].dmM > vector[3].dmM > vector[4].dmM and vector[5].close > vector[2].maxC):
            vector[5].P.append(79)          #Bullish squeeze alert
            return

        if ( ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue) or None)
                and (vector[2].candleType == 1 or 2) and vector[2].open < vector[2].close
                and vector[2].minC < (max(vector[3].open, vector[3].close)) < vector[2].maxC
                and vector[3].minC < max(vector[4].open, vector[4].close) < vector[3].maxC
                and vector[2].dmM > vector[3].dmM > vector[4].dmM and vector[5].close < vector[2].minC):
            vector[5].P.append(80)          # Bearish squeeze alert
            return


        # Pattern di continuazione

        if (((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue) or None)
                and vector[3].CBR >= 2
                and vector[3].open < vector[3].close
                and vector[4].minC > vector[3].maxC
                and vector[4].open < vector[4].close
                and vector[5].open > vector[5].close
                and vector[4].open < vector[5].open < vector[4].close
                and vector[3].maxC < vector[5].close < vector[4].close
                and vector[3].boc < vector[4].boc):
            vector[5].P.append(98)          #Upside Tasuki gap
            return

        if (((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue) or None)
                and vector[3].CBR >= 2
                and vector[3].open > vector[3].close
                and vector[4].maxC < vector[3].minC
                and vector[4].open > vector[4].close
                and vector[5].open < vector[5].close
                and vector[4].close < vector[5].open < vector[4].open
                and vector[4].maxC < vector[5].close < vector[3].minC
                and vector[3].boc < vector[4].boc):
            vector[5].P.append(99)          # Downside Tasuki gap
            return

        if (((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue) or None)
                and vector[3].CBR >= 2
                and vector[3].open < vector[3].close
                and vector[4].open >= vector[3].maxC
                and vector[4].open < vector[4].close
                and vector[5].open < vector[5].close
                and vector[5].open < vector[4].close
                and abs(vector[5].open - vector[4].open) < (vector[4].doc / 2)
                and vector[3].boc < vector[4].boc):
            vector[5].P.append(100)         #Side by side green line Bullish
            return

        if (((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue) or None)
                and vector[3].CBR >= 2
                and vector[3].open > vector[3].close
                and vector[4].open <= vector[3].minC
                and vector[4].open < vector[4].close
                and vector[5].open < vector[5].close
                and vector[5].open >= vector[4].open
                and abs(vector[5].close - vector[4].close) < (vector[4].doc / 2)
                and vector[3].boc > vector[4].boc):
            vector[5].P.append(101)         #Side by side green lines Bearish
            return

        if (((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue) or None)
                and vector[3].CBR >= 2
                and vector[3].open < vector[3].close
                and vector[4].open > vector[4].close
                and vector[4].open > vector[3].close
                and vector[4] >= vector[3].close
                and vector[5].open > vector[4].boc
                and vector[5].open > vector[4].close
                and vector[5].close >= vector[3].close
                and vector[3].boc < vector[4].boc):
            vector[5].P.append(102)         # Side by side red lines Bullish
            return

        if (((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue) or None)
                and vector[3].CBR >= 2
                and vector[3].open > vector[3].close
                and vector[4].open > vector[4].close
                and vector[4].open < vector[3].close
                and vector[5].open > vector[4].boc
                and vector[5].open > vector[5].close
                and vector[5].close < vector[3].close
                and vector[3].boc > vector[4].boc):
            vector[5].P.append(103)         #Side by side red lines Bearish
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                and vector[3].CBR >= 4
                and vector[4].CBR >= 2
                and vector[3].open < vector[3].close
                and vector[4].open < vector[4].close
                and vector[4].open > vector[3].maxC
                and vector[4].close > vector[3].close
                and vector[4].open < vector[5].open < vector[4].close
                and vector[5].open > vector[5].close
                and vector[5].close < vector[3].boc
                and vector[5].boc < vector[4].boc):
            vector[5].P.append(104)         #Upside three methods bullish
            return

        if ((vector[0].EMAvalue >= vector[1].EMAvalue >= vector[2].EMAvalue >= vector[3].EMAvalue >= vector[4].EMAvalue)
                and vector[3].CBR >= 4
                and vector[4].CBR >= 2
                and vector[3].open > vector[3].close
                and vector[4].open > vector[4].close
                and vector[4].open < vector[3].minC
                and vector[5].open < vector[5].close
                and vector[4].close < vector[5].open < vector[4].open
                and vector[5].close > vector[3].close
                and vector[5].boc > vector[4].boc):
            vector[5].P.append(105)         #Downside three methods Bearish
            return

        if ((vector[0].EMAvalue <= vector[1].EMAvalue <= vector[2].EMAvalue <= vector[3].EMAvalue <= vector[4].EMAvalue)
                and vector[3].CBR >= 4
                and vector[3].open < vector[3].close
                and vector[3].dmM > (sum(vector[2].dmM, vector[1].dmM, vector[0].dmM) / 3)   # ???
                and vector[4].dmM < 0.75 * vector[3].dmM
                and vector[5].dmM < 0.75 * vector[3].dmM
                and vector[4].CBR <= 3
                and vector[5].CBR <= 3
                and vector[4] > vector[3].bmM
                and vector[5].close > vector[3].bmM
                and vector[5].minC > vector[3].bmM
                and vector[4].maxC > vector[3].close
                and vector[4].minC < vector[3].maxC
                and vector[5].open < vector[4].maxC
                and vector[5].close < vector[4].maxC):
            vector[5].P.append(106)         #Rest after battle
            return

        vector[5].P.append(0)
        return








