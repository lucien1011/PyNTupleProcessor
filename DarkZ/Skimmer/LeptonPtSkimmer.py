from Core.Module import Module

class LeptonPtSkimmer(Module):
    def analyze(self,event):
        if event.leps[0].pt < 20: return False
        if event.leps[1].pt < 10: return False
        return True
