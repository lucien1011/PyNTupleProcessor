import ROOT

class Object(object):
    """Class that allows seeing a set branches plus possibly an index as an Object"""
    def __init__(self,event,objName,index):
        self._event   = event
        self._objName = objName+"_"
        self._index   = index
        self._p4      = None
        pass

    def __getattr__(self,quantity):
        if quantity != "phyLabel":
            return getattr(self._event,self._objName+quantity)[self._index]
        else:
            return self._objName[:-1] 

    def p4(self):
        if self._p4 == None:
            self._p4 = ROOT.TLorentzVector()
            self._p4.SetPtEtaPhiM(self.pt,self.eta,self.phi,self.mass)
            pass
        return self._p4
        pass

class Collection(object):
    def __init__(self,event,objName):
        self._event   = event   
        self._objName = objName
        self._phyDict = {}
        self._validateInput()

    def __getitem__(self,index):
        if index >= len(self):
            raise IndexError
        else:
            if index not in self._phyDict:
                self._phyDict[index] = Object(self._event,self._objName,index)
            return self._phyDict[index]

    def __len__(self):
        # probably a hack
        return len(getattr(self._event,self._objName+"_pt"))

    def _validateInput(self):
        if not hasattr(self._event,self._objName+"_pt"):
            raise AttributeError, "Object {} does not exist in tree".format(self._objName)
