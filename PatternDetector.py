class PatternDetector:

    candleVector=[]

    def addCandleToVector(self, GenCadle):

        if len(self.candleVector)==8: self.candleVector.pop(0)
        self.candleVector.append(GenCadle)

    def determinePatterns(self):