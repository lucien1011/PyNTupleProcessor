from Core.Module import Module

class METSkimmer(Module):
    def analyze(self,event):
        return event.met_pt[0] > 50
