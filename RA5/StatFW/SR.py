class SR(object):
    def __init__(self,number,lepCat):
        self.number = number
        self.lepCat = lepCat

    def getBinName(self):
        return self.lepCat+"_SR"+str(self.number)
