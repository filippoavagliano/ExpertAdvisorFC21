from FivePatternDetector import FivePatternDetector
from FourPatternDetector import FourPatternDetector
from OnePatternDetector import OnePatternDetector
from ThreePatternDetector import ThreePatternDetector
from TwoPatternDetector import TwoPatternDetector


candleVector = []
patternNames = []

def addCandleToVector(genCandle):
    if len(candleVector) == 8: candleVector.pop(0)
    candleVector.append(genCandle)

def determinePatterns():
    OnePatternDetector.determinePattern(candleVector)
    TwoPatternDetector.determinePattern(candleVector)
    ThreePatternDetector.determinePattern(candleVector)
    FourPatternDetector.determinePattern(candleVector)
    FivePatternDetector.determinePattern(candleVector)
    print(candleVector[-1].P)