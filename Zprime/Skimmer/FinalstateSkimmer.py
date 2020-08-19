from Core.Module import Module
import ROOT as r

class FinalstateSkimmer(Module):
    def __init__(self,name):
        super(FinalstateSkimmer,self).__init__(name)
        
    def analyze(self,event):
        if ("Data2017" in self.dataset.name) or ("WZTo3LNu" in self.dataset.name) or ("TTJets" in self.dataset.name) or ("DYJetsToLL_M50" in self.dataset.name) or ("DYJetsToLL_M10To50" in self.dataset.name):
            if abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13 and event.IsoL3[0] < 0.35 and 1.4 < abs(event.etaL3[0]) <= 2.5:
                return True
            elif abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13 and event.IsoL3[0] < 0.35 and 1.4 < abs(event.etaL3[0]) <= 2.5:
                return True
            else:
                return False
        if ("dataSamples" in self.dataset.name):
            if abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13 and event.IsoL3[0] < 0.35 and 1.4 < abs(event.etaL3[0]) <= 2.5:
                return True
            elif abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13 and event.IsoL3[0] < 0.35 and 1.4 < abs(event.etaL3[0]) <= 2.5:
                return True
            else:
                return False
        return True
