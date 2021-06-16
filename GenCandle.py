

class GenCandle:
    open = 0
    close = 0
    maxC = 0
    minC = 0
    mMdistances = []  # list of the last 20 shadow distances
    ocdistances = []  # list of the last 20 open-close distances
    doc = 0  # open close distance
    dmM = 0  # shadows distance
    ts = 0  # top shadow
    bs = 0  # bottom shadow
    boc = 0  # open close baricenter
    bmM = 0  # shadows baricenter
    dbb = 0  # baricenters distance
    S = 0  # asimmetry coefficient
    r = 0  # fullness factor
    COR = 0  # Candle Oscillator Range
    CBR = 0  # Candle Body Range
    Tr = 0  # Trend index
    P = []  # Patterns vector

    mb = 0  # min of open-close
    Mb = 0  # max of open-close

    MdmM = 0
    mdmM = 0
    avgdmM = 0
    MavgdmM = 0
    mavgdmM = 0
    Mdoc = 0
    mdoc = 0
    avgdoc = 0
    Mavgdoc = 0
    mavgdoc = 0

    lastClose = 0  # last candle close value
    bollBw = 0  # Bollinger bands bandwidth

    EMAvalue = 0  # Exponential Moving Average value up to this point

    candleType = 0  # Candle type id

    # mMdistances=lista delle distanze delle ombre dalle 20 candele precedenti
    # ocdistances=lista delle distanze tra open e close dalle 20 candele precedenti
    # lastClose=prezzo di chiusura dell'ultima candela chiusa
    # bollBw=larghezza di banda delle bande di Bollinger

    def __init__(self, open, close, maxC, minC, mMdistances, ocdistances, lastClose, bollBw, EMA):

        self.open = round(open, 5)
        self.close = close
        self.maxC = round(maxC, 5)
        self.minC = round(minC, 5)
        self.mMdistances = mMdistances
        self.ocdistances = ocdistances
        self.lastClose = lastClose
        self.bollBw = round(bollBw, 5)
        self.EMAvalue = round(EMA, 5)
        self.doc = round(abs(open - close), 5)
        self.dmM = round(abs(maxC - minC), 5)
        self.ts = round(maxC - max(open, close), 5)
        self.bs = round(min(open, close) - minC, 5)
        self.boc = round((open + close) / 2, 5)
        self.bmM = round((minC + maxC) / 2, 5)
        self.dbb = round(abs(self.boc - self.bmM), 5)
        self.r = round(self.doc / self.dmM, 5)
        self.mb = min(open, close)
        self.Mb = max(open, close)
        self.MdmM = round(self.calcMdmM(), 5)
        self.mdmM = round(self.calcmdmM(), 5)
        self.avgdmM = round(self.calcavgdmM(), 5)
        self.MavgdmM = round(self.calcMavgdmM(), 5)
        self.mavgdmM = round(self.calcmavgdmM(), 5)
        self.Mdoc = round(self.calcMdoc(), 5)
        self.mdoc = round(self.calcmdoc(), 5)
        self.avgdoc = round(self.calcavgdoc(), 5)
        self.Mavgdoc = round(self.calcMavgdoc(), 5)
        self.mavgdoc = round(self.calcmavgdoc(), 5)
        self.S = self.calcS()
        self.COR = self.calcCOR()
        self.CBR = self.calcCBR()
        self.Tr = self.calcTr()

        self.candleType = self.detType()

    @staticmethod
    def calcSR(bs, ts):

        return (ts - bs) / (ts + bs)

    def calcS(self):

        sr = self.calcSR(self.bs, self.ts)
        print("Sr ", sr)
        if 0.6 < sr <= 1:
            return 2  # High top asimmetry
        if 0.2 < sr <= 0.6:
            return 1  # Top asimmetry
        if -0.2 <= sr <= 0.2:
            return 0  # Simmetry
        if -0.6 <= sr < -0.2:
            return -1  # Bottom asimmetry
        if -1 <= sr < -0.6:
            return -2  # High bottom asimmetry

    def calcMdmM(self):  # max of the last 20 shadow distances

        return max(self.mMdistances)

    def calcmdmM(self):  # min of the last 20 shadow distances

        return min(self.mMdistances)

    def calcavgdmM(self):  # average of the last 20 shadow distances

        return sum(self.mMdistances) / 20

    def calcMavgdmM(self):  # near high level of decision of the last 20 shadow distances

        return (self.MdmM + self.avgdmM) / 2

    def calcmavgdmM(self):  # near low level of decision of the last 20 shadow distances

        return (self.mdmM + self.avgdmM) / 2

    def dmMVect(self):

        return [self.MdmM, self.MavgdmM, self.avgdmM, self.mavgdmM, self.mdmM]

    def ddmM(self):

        return min(abs(self.dmM - self.MdmM), abs(self.dmM - self.MavgdmM), abs(self.dmM - self.avgdmM),
                   abs(self.dmM - self.mavgdmM), abs(self.dmM - self.mdmM))

    def calcCOR(self):

        ddmM = self.ddmM()
        if ddmM == abs(self.dmM - self.mdmM):
            return 1  # very short oscillator
        if ddmM == abs(self.dmM - self.mavgdmM):
            return 2  # short oscillator
        if ddmM == abs(self.dmM - self.avgdmM):
            return 3  # medium oscillator
        if ddmM == abs(self.dmM - self.MavgdmM):
            return 4  # long oscillator
        if ddmM == abs(self.dmM - self.MdmM):
            return 5  # very long oscillator

    def calcMdoc(self):  # max of the last 20 open-close distances

        return max(self.ocdistances)

    def calcmdoc(self):  # min of the last 20 open-close distances

        return min(self.ocdistances)

    def calcavgdoc(self):  # average of the last 20 open-close distances

        return sum(self.ocdistances) / 20

    def calcMavgdoc(self):  # near high level of decision of the last 20 open-close distances

        return (self.Mdoc + self.avgdoc) / 2

    def calcmavgdoc(self):  # near low level of decision of the last 20 open-close distances

        return (self.mdoc + self.avgdoc) / 2

    def ddoc(self):

        return min(abs(self.doc - self.Mdoc), abs(self.doc - self.Mavgdoc), abs(self.doc - self.avgdoc),
                   abs(self.doc - self.mavgdoc), abs(self.doc - self.mdoc))

    def calcCBR(self):

        ddoc = self.ddoc()
        if ddoc == abs(self.doc - self.mdoc):
            return 1  # very short range
        if ddoc == abs(self.doc - self.mavgdoc):
            return 2  # short range
        if ddoc == abs(self.doc - self.avgdoc):
            return 3  # medium range
        if ddoc == abs(self.doc - self.Mavgdoc):
            return 4  # long range
        if ddoc == abs(self.doc - self.Mdoc):
            return 5  # very long range

    def removeDPoint(self, n):

        n = str(n)
        intPart = n.split('.')[0]
        print("int ", intPart)
        decPart = n.split('.')[1]
        print("dec ", decPart)

        n = f"{intPart}{decPart}"
        if n.__len__()!=6:
            n = f"{n}{'0'}"
            print(int(n))
            return int(n)

        return int(f"{intPart}{decPart}")

    def calcTr(self):

        close = self.removeDPoint(self.close)
        lastClose = self.removeDPoint(self.lastClose)

        dPip = abs(close - lastClose)

        if (40 / (3 * self.bollBw)) <= dPip < (40 / (2 * self.bollBw)):
            return 5
        if (40 / (4 * self.bollBw)) <= dPip < (40 / (3 * self.bollBw)):
            return 4
        if (40 / (6 * self.bollBw)) <= dPip < (40 / (4 * self.bollBw)):
            return 3
        if (40 / (18 * self.bollBw)) <= dPip < (40 / (6 * self.bollBw)):
            return 2
        if 0 <= dPip < (40 / (18 * self.bollBw)):
            return 1
        if (-40 / (18 * self.bollBw)) <= dPip < 0:
            return -1
        if (-40 / (6 * self.bollBw)) <= dPip < (-40 / (18 * self.bollBw)):
            return -2
        if (-40 / (4 * self.bollBw)) <= dPip < (-40 / (6 * self.bollBw)):
            return -3
        if (-40 / (3 * self.bollBw)) <= dPip < (-40 / (4 * self.bollBw)):
            return -4
        if (-40 / (2 * self.bollBw)) <= dPip < (-40 / (3 * self.bollBw)):
            return -5

    def detType(self):

        if self.CBR == 5 and self.bs >= (2 * self.ts): return 4     # 4-Closing Bullish Marubozu/Opening Bearish Marubozu
        if self.CBR == 5 and self.ts >= (2 * self.bs): return 5     # 5-Closing Bearish Marubozu/Opening Bullish Marubozu
        if self.doc / self.dmM > 0.8: return 3                      # 3-Marubozu
        if (1 < self.CBR <= 3) and (-1 <= self.S <= 1): return 6    # 6-Spinning top
        if (1 <= self.CBR <= 4) and (self.boc > self.bmM) and self.S == -2 and self.open < self.close:
            return 12                                               # 12-Bullish Paper Umbrella
        if (1 <= self.CBR <= 4) and (self.boc > self.bmM) and self.S == -2 and self.open > self.close:
            return 13                                               # 13-Bearish Paper Umbrella
        if (1 <= self.CBR <= 4) and (self.boc < self.bmM) and self.S == 2 and self.open < self.close:
            return 14                                               # 14-Reversal Bullish Paper Umbrella
        if (1 <= self.CBR <= 4) and (self.boc < self.bmM) and self.S == 2 and self.open > self.close:
            return 15                                               # 15-Reversal Bearish Paper Umbrella
        if self.CBR == 1 and (-1 <= self.S <= 1): return 8          # 8-Long-legged Doji
        if self.CBR == 1 and self.S >= 1: return 9                  # 9-Gravestone Doji
        if self.CBR == 1 and self.S <= -1: return 10                # 10-Dragonfly Doji
        if self.CBR == 1 and self.S == 0: return 11                 # 11-Four Price Doji
        if self.CBR == 1: return 7  # 7-Doji
        if self.CBR >= 4: return 1                                  # 1-Long range
        if self.CBR <= 2: return 2                                  # 2-Short range


    def toString(self):

        print("open ", self.open)
        print("close ", self.close)
        print("max ", self.maxC)
        print("minc ", self.minC)
        print("mMdistance ", self.mMdistances)
        print("oCdistance ", self.ocdistances)
        print("avgdmM ", self.avgdmM)
        print("MavgdmM ", self.MavgdmM)
        print("mavgdmM ", self.mavgdmM)
        print("Mdoc ", self.Mdoc)
        print("mdoc ", self.mdoc)
        print("avgdoc ", self.avgdoc)
        print("Mavgdoc ", self.Mavgdoc)
        print("mavgdoc ", self.mavgdoc)
        print("lastclose ", self.lastClose)
        print("bollBw ", self.bollBw)
        print("EMAvalue ", self.EMAvalue)
        print("bs ", self.bs)
        print("ts ", self.ts)
        print("Tr ", self.Tr)
        print("doc ", self.doc)
        print("dmM ", self.dmM)
        print("boc ", self.boc)
        print("bmM ", self.bmM)
        print("CBR ", self.CBR)
        print("S ", self.S)
        print("mb ", self.mb)
        print("Mb ", self.Mb)
        print("MdmM ", self.MdmM)
        print("mdmM ", self.mdmM)

        print("candleType ", self.candleType)
        return




