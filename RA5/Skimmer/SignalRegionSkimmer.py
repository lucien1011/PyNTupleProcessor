from Core.Module import Module

class SignalRegionSkimmer(Module):
    def analyze(self,event):
        if event.met_pt[0] < 50.: return False
        return True
