from Core.Module import Module

from DarkZ.Common.HZZAlgo import HZZAlgo

class Z1Z2Skimmer(Module):
    def __init__(self,name):
        super(Z1Z2Skimmer,self).__init__(name)
        self.HZZAlgo = HZZAlgo()

    def analyze(self,event):
        event.ZCandidates = self.HZZAlgo.makeZCandidatesFromCollection(event.leps,useFSR=True)
        Z1,Z2,passZ1Z2 = self.HZZAlgo.makeZ1Z2(event.ZCandidates,[40.,120.],[12.,120.]) 
        #if Z1.vec.M() < 40 or Z1.vec.M() > 120: return False
        #if Z2.vec.M() < 12 or Z2.vec.M() > 120: return False
        event.Z1 = Z1
        event.Z2 = Z2
        if not passZ1Z2: return False
        return True
