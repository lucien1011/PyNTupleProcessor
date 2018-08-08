from Core.Module import Module

class AnalysisSkimmer(Module):
    def __init__(self,name,cutflow="DarkPhoton-SR"):
        super(AnalysisSkimmer,self).__init__(name)
        self.cutflow = cutflow

    def analyze(self,event):
        if self.cutflow == "DarkPhoton-SR":
            #if event.mass4l[0] < 118. or event.mass4l[0] > 130.: return False
            if event.mass4l[0] < 105. or event.mass4l[0] > 140.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            if not event.passedFullSelection[0]: return False
            return True
        elif self.cutflow == "DarkPhoton-ZXCR":
            if not event.passedZXCRSelection[0]: return False
            if event.mass4l[0] < 105. or event.mass4l[0] > 140.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            return True
        elif self.cutflow == "Higgs-SR":
            if event.mass4l[0] < 70.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
            if not event.passedFullSelection[0]: return False
            return True
        elif self.cutflow == "Higgs-ZXCR":
            if not event.passedZXCRSelection[0]: return False
            if event.mass4l[0] < 70.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
            return True
        elif self.cutflow == "Higgs-m4lSB":
            if event.mass4l[0] > 118. and event.mass4l[0] < 130.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            if not event.passedFullSelection[0]: return False
        return True
