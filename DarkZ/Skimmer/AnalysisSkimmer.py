from Core.Module import Module

class AnalysisSkimmer(Module):

    def analyze(self,event):
        #if event.mass4l[0] < 118. or event.mass4l[0] > 130.: return False
        if event.mass4l[0] < 105. or event.mass4l[0] > 140.: return False
        
        #if event.massZ1[0] < 40. or event.massZ1[0] > 120.: return False
        
        #if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
        #if event.massZ2[0] < 12. or event.massZ2[0] > 120.: return False
        
        #if not event.passSmartCut[0]: return False
        #if not event.passedFullSelection[0]: return False
        if not event.passedZXCRSelection[0]: return False
        return True
