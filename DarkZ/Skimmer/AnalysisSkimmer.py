from Core.Module import Module

class AnalysisSkimmer(Module):
    def __init__(self,name,cutflow="DarkPhoton-SR"):
        super(AnalysisSkimmer,self).__init__(name)
        self.cutflow = cutflow

    def analyze(self,event):
        if self.cutflow == "DarkPhoton-SR":
            if event.mass4l[0] < 118. or event.mass4l[0] > 130.: return False
            #if event.mass4l[0] < 105. or event.mass4l[0] > 140.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            if "ZPlusX" not in self.dataset.name:
                if not event.passedFullSelection[0]: return False
            return True
        elif self.cutflow == "DarkPhoton-m4lSB":
            if not ((event.mass4l[0]>105. and event.mass4l[0]<118.) or (event.mass4l[0]>130. and event.mass4l[0]<140.)): return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            if "ZPlusX" not in self.dataset.name:
                if not event.passedFullSelection[0]: return False
            return True
        elif self.cutflow == "DarkPhoton-ZXCR":
            if not event.passedZXCRSelection[0]: return False
            if event.mass4l[0] < 105. or event.mass4l[0] > 140.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            return True
        elif self.cutflow == "DarkPhoton-ZXCR-v2":
            if not event.passedZXCRSelection[0]: return False
            #if event.mass4l[0] < 105. or event.mass4l[0] > 140.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            return True
        elif self.cutflow == "Higgs-SR":
            if event.mass4l[0] < 70.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
            if "ZPlusX" not in self.dataset.name:
                if not event.passedFullSelection[0]: return False
            return True
        elif self.cutflow == "Higgs-ZXCR":
            if not event.passedZXCRSelection[0]: return False
            if event.mass4l[0] < 70.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
            return True
        elif self.cutflow == "Higgs-3P1F":
            if not event.passedZXCRSelection[0]: return False
            if "PredCR" not in self.dataset.name:
                if event.nZXCRFailedLeptons[0] != 1: return False 
            if event.mass4l[0] < 70.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
            return True
        elif self.cutflow == "Higgs-m4lSB":
            if event.mass4l[0] > 120. and event.mass4l[0] < 130.: return False
            if event.mass4l[0] < 110. or event.mass4l[0] > 140.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
            if "ZPlusX" not in self.dataset.name:
                if not event.passedFullSelection[0]: return False
            return True
        elif self.cutflow == "Higgs-m4lNarrowWindow":
            if event.mass4l[0] < 118. or event.mass4l[0] > 130.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
            if "ZPlusX" not in self.dataset.name:
                if not event.passedFullSelection[0]: return False
            return True
        elif self.cutflow == "Upsilon-CR":
            if event.mass4l[0] > 118. and event.mass4l[0] < 130.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            #if "ZPlusX" not in self.dataset.name:
            #    if not event.passedFullSelection[0]: return False
            return True
        elif self.cutflow == "WrongFC-CR":
            if event.mass4l[0] < 118. or event.mass4l[0] > 130.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            if event.passedFullSelection[0]: return False
            return True
        elif self.cutflow == "WrongFC-SR":
            #if event.mass4l[0] < 118. or event.mass4l[0] > 130.: return False
            #if event.mass4l[0] < 70.: return False
            if event.mass4l[0] < 108. or event.mass4l[0] > 140.: return False
            if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            #if event.passedZXCRSelection[0]: return False
            return True
        return False
