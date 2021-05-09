class GenCandle:

    open=0
    close=0
    maxC=0
    minC=0
    mMdistances=[]  # list of the last 20 shadow distances
    ocdistances=[]  # list of the last 20 open-close distances
    doc=0           # open close distance
    dmM=0           # shadows distance
    ts=0            # top shadow
    bs=0            # bottom shadow
    boc=0           # open close baricenter
    bmM=0           # shadows baricenter
    dbb=0           # baricenters distance
    S=0             # asimmetry coefficient
    r=0             # fullness factor
    COR=0           # Candle Oscillator Range
    CBR=0           # Candle Body Range
    Tr=0            # Trend index
    P=0             # part of pattern

    MdmM=0
    mdmM=0
    avgdmM=0
    MavgdmM=0
    mavgdmM=0

    def __init__(self,open,close,maxC,minC,mMdistances,ocdistances):

        self.open=open
        self.close=close
        self.maxC=maxC
        self.minC=minC
        self.mMdistances=mMdistances
        self.ocdistances=ocdistances
        self.doc=abs(open-close)
        self.dmM=abs(maxC-minC)
        self.ts=maxC-max(open,close)
        self.bs=min(open,close)-minC
        self.boc=(open+close)/2
        self.bmM=(minC+maxC)/2
        self.dbb=abs(self.boc-self.bmM)
        self.S=self.calcS()
        self.r=self.doc/self.dmM
        self.COR=self.calcCOR()
        self.CBR=self.calcCBR()

        self.MdmM=self.calcMdmM()
        self.mdmM=self.calcmdmM()
        self.avgdmM=self.calcavgdmM()
        self.MavgdmM=self.calcMavgdmM()
        self.mavgdmM=self.calcmavgdmM()

        self.Mdoc = self.calcMdoc()
        self.mdoc = self.calcmdoc()
        self.avgdoc = self.calcavgdoc()
        self.Mavgdoc = self.calcMavgdoc()
        self.mavgdoc = self.calcmavgdoc()

    def SR(self,bs,ts):

        return (ts-bs)/(ts+bs)

    def calcS(self):

        sr=self.SR(self.bs, self.tr)

        if sr>0.6 and sr<=1:
            return 2     # High top asimmetry
        if sr>0.2 and sr<=0.6:
            return 1     # Top asimmetry
        if sr>=-0.2 and sr<=0.2:
            return 0     # Simmetry
        if sr>=-0.6 and sr<-0.2:
            return -1    # Bottom asimmetry
        if sr>=-1 and sr<-0.6:
            return -2    # High bottom asimmetry

    def calcMdmM(self):      # max of the last 20 shadow distances

        return max(self.mMdistances)

    def calcmdmM(self):     # min of the last 20 shadow distances

        return min(self.mMdistances)

    def calcavgdmM(self):   # average of the last 20 shadow distances

        return sum(self.mMdistances) / 20

    def calcMavgdmM(self):  # near high level of decision of the last 20 shadow distances

        return (self.MdmM+self.avgdmM)/2

    def calcmavgdmM(self):  # near low level of decision of the last 20 shadow distances

        return (self.mdmM+self.avgdmM)/2

    def dmMVect(self):

        return [self.MdmM,self.MavgdmM,self.avgdmM,self.mavgdmM,self.mdmM]

    def ddmM(self):

        return min(abs(self.dmM-self.MdmM),abs(self.dmM-self.MavgdmM),abs(self.dmM-self.avgdmM),abs(self.dmM-self.mavgdmM),abs(self.dmM-self.mdmM))

    def calcCOR(self):

        ddmM=self.ddmM()
        if ddmM==abs(self.dmM-self.mdmM):
            return 1        # very short oscillator
        if ddmM==abs(self.dmM-self.mavgdmM):
            return 2        # short oscillator
        if ddmM==abs(self.dmM-self.avgdmM):
            return 3        # medium oscillator
        if ddmM==abs(self.dmM-self.MavgdmM):
            return 4        # long oscillator
        if ddmM==abs(self.dmM-self.MdmM):
            return 5        # very long oscillator

    def calcMdoc(self):      # max of the last 20 open-close distances

        return max(self.ocdistances)

    def calcmdoc(self):     # min of the last 20 open-close distances

        return min(self.ocdistances)

    def calcavgdoc(self):   # average of the last 20 open-close distances

        return sum(self.ocdistances) / 20

    def calcMavgdoc(self):  # near high level of decision of the last 20 open-close distances

        return (self.Mdoc+self.avgdoc)/2

    def calcmavgdoc(self):  # near low level of decision of the last 20 open-close distances

        return (self.mdoc+self.avgdoc)/2

    def ddoc(self):

        return min(abs(self.doc-self.Mdoc),abs(self.doc-self.Mavgdoc),abs(self.doc-self.avgdoc),abs(self.doc-self.mavgdoc),abs(self.doc-self.mdoc))

    def calcCBR(self):

        ddoc=self.ddoc()
        if ddoc==abs(self.doc-self.mdoc):
            return 1        # very short range
        if ddoc==abs(self.doc-self.mavgdoc):
            return 2        # short range
        if ddoc==abs(self.doc-self.avgdoc):
            return 3        # medium range
        if ddoc==abs(self.doc-self.Mavgdoc):
            return 4        # long range
        if ddoc==abs(self.doc-self.Mdoc):
            return 5        # very long range