from GenCandle import *
class OneCandlePattern:

    def determinePattern(self, candleVector):

        vector=candleVector[-1:-4]

        if ((vector[3].getEMA() <= vector[2].getEMA() <= vector[1].getEMA() <= vector[0].getEMA)
                    and (vector[3].candleType == 12 or vector[3].candleType == 13)):
            vector[3].P.append(24)



