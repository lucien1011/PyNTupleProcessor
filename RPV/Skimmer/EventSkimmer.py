from Core.Module import Module

class EventSkimmer(Module):
    def __init__(self,name,csvCut=0.8484,cutflow="LooseSignal"):
        self.csvCut = csvCut
        self.cutflow = cutflow

    def analyze(self,event):
        if self.cutflow == "LooseSignal":
            return self.makeCommonSelection(event)
        elif self.cutflow == "htCR":
            return self.makeCommonSelection(event) and event.ht40 < 800.
        else:
            raise RuntimeError, "Cutflow "+self.cutflow+" not supported"

    def makeCommonSelection(self,event):
        if event.nJet40 < 2: return False
        if event.nLep40 < 2: return False
        if event.jets[0].btagCSVV2 < self.csvCut and event.jets[1].btagCSVV2 < self.csvCut: return False
        if event.leps[0].charge == event.leps[1].charge: return False
        if event.mll and event.mll < 300: return False
        return True

