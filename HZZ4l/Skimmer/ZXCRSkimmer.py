from Core.Module import Module

class ZXCRSkimmer(Module):
    def analyze(self,event):
        if not event.passedZXCRSelection[0]: return False
        if "PredCR" not in self.dataset.name:
            try: 
                if event.nZXCRFailedLeptons[0] != 1: return False 
            except AttributeError: 
                #event.nZXCRFailedLeptons = event.nFailedLeptonsZ2
                if event.nZXCRFailedLeptons[0] != 1: return False 
        #if event.mass4l[0] < 118. or event.mass4l[0] > 130.: return False
        if event.mass4l[0] < 70.: return False
        if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
        if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
        return True
