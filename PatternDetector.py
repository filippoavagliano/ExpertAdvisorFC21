from FivePatternDetector import FivePatternDetector
from FourPatternDetector import FourPatternDetector
from OnePatternDetector import OnePatternDetector
from ThreePatternDetector import ThreePatternDetector
from TwoPatternDetector import TwoPatternDetector


candleVector = []
patternNames = []

def addCandleToVector(self, genCandle):
    if len(self.candleVector) == 8: self.candleVector.pop(0)
    self.candleVector.append(genCandle)

@staticmethod
def determinePatterns():
    OnePatternDetector.determinePattern(candleVector)
    TwoPatternDetector.determinePattern(candleVector)
    ThreePatternDetector.determinePattern(candleVector)
    FourPatternDetector.determinePattern(candleVector)
    FivePatternDetector.determinePattern(candleVector)
    print(candleVector[-1].P)