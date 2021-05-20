class ThreePatternDetector:

    @staticmethod
    def determinePattern(candleVector):

        vector = candleVector[-1:-6]
        type = vector[5].candleType

        if ((vector[5].EMAvalue >= vector[4].EMAvalue >= vector[3].EMAvalue >= vector[2].EMAvalue >= vector[1].EMAvalue
            >= vector[0].EMAvalue) and vector[3].candleType == 1 and vector[5].CBR >= 2 and vector[3].open > vector[3].close
            > vector[4].Mb