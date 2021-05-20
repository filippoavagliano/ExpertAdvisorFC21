from OnePatternDetector import OnePatternDetector
from TwoPatternDetector import TwoPatternDetector

class PatternDetector:
    candleVector = []
    patternNames = []

    def addCandleToVector(self, genCandle):
        if len(self.candleVector) == 8: self.candleVector.pop(0)
        self.candleVector.append(genCandle)

    def determinePatterns(self, candlevVec):
        OnePatternDetector.determinePattern(candlevVec)
        TwoPatternDetector.determinePattern()
