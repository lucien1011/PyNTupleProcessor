
from Core.Module import Module

class AnalysisSkimmer(Module):
    def __init__(self,name,cutflow="Zprime-SR"):
        super(AnalysisSkimmer,self).__init__(name)
        self.cutflow = cutflow

    def analyze(self,event):
        if self.cutflow == "Zprime-SR":
            if event.mass4l[0] < 80. or event.mass4l[0] > 100.: return False
            if event.massZ1[0] < 12. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            if event.mass4mu[0] < 0.: return False
            if not event.passedFullSelection[0]: return False
            if not (abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13): return False
            return True
        elif self.cutflow == "Zprime-m4lCR":
            if event.mass4l[0] > 80. and event.mass4l[0] < 100.: return False
            if event.massZ1[0] < 12. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            if event.mass4mu[0] < 0.: return False
            if not event.passedFullSelection[0]: return False
            if not (abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13): return False
        return False
