
from Core.Module import Module

class AnalysisSkimmer(Module):
    def __init__(self,name,cutflow="Zprime-SR"):
        super(AnalysisSkimmer,self).__init__(name)
        self.cutflow = cutflow

    def analyze(self,event):
        if self.cutflow == "Zprime-SR":
            if event.mass4l[0] < 80. or event.mass4l[0] > 100.: return False
            #if event.mass4l[0] < 100. and event.mass4l[0] > 80.: return False
            #if event.mass4l[0] < 70.: return False
            if event.massZ1[0] < 12. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 1. or event.massZ2[0] > 120.: return False
            #if not event.passedFullSelection[0]: return False
            if event.nZXCRFailedLeptons[0] != 1: return False
            return True
        return False
