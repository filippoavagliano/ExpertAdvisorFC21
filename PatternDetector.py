import GenCandle
from OnePatternDetector import OnePatternDetector
from TwoPatternDetector import TwoPatternDetector


class PatternDetector:

    candleVector=[]
    patternNames=[]

    def addCandleToVector(self, genCandle):

        if len(self.candleVector)==8: self.candleVector.pop(0)
        self.candleVector.append(genCandle)

    def determinePatterns(self, candlevVec):

        g: GenCandle=candlevVec[7]
        OnePatternDetector.determinePattern(candlevVec,g.candleType)
        TwoPatternDetector.determinePattern(candlevVec,g.candleType)