class Syst(object):
    def __init__(self,name,factorFunc):
        self.name = name
        self.factorFunc = factorFunc

    def getWeight(self,event):
        return self.factorFunc(event)

