from Core.Module import Module

class METSkimmer(Module):
    def __init__(self,name,invert=False):
        super(METSkimmer,self).__init__(name)
        self.invert = invert
        self.metCut = 50.

    def analyze(self,event):
        if self.invert:
            return event.met_pt[0] < self.metCut
        else:
            return event.met_pt[0] > self.metCut
