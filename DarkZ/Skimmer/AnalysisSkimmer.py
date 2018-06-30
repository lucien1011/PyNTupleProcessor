from Core.Module import Module

class AnalysisSkimmer(Module):

    def analyze(self,event):
        if event.mass4l[0] < 115 or event.mass4l[0] > 130: return False
        if event.massZ1[0] < 80 or event.massZ1[0] > 100: return False
        if event.massZ2[0] < 15 or event.massZ2[0] > 115: return False
        return True
