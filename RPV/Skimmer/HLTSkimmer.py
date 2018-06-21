from Core.Module import Module

class HLTSkimmer(Module):
    def __init__(self,name,cutflow="LooseSignal"):
        super(HLTSkimmer,self).__init__(name)
        self.cutflow = cutflow

    def analyze(self,event):
        return event.HLT_IsoMu22[0] or event.HLT_IsoTkMu22[0] or event.HLT_IsoMu24[0] or event.HLT_IsoTkMu24[0]
