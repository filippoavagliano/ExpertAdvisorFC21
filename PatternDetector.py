import OnePatternDetector

class PatternDetector:

    candleVector=[]

    def addCandleToVector(self, genCandle):

        if len(self.candleVector)==8: self.candleVector.pop(0)
        self.candleVector.append(genCandle)

    def determinePatterns(self, candlevVec):

        OnePatternDetector.determinePattern(candlevVec)