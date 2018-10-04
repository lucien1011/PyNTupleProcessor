from Core.Module import Module

class GammaCRSkimmer(Module):
    def analyze(self,event):
        return True

class GammaCRTreeSkimmer(Module):
    def analyze(self,event):
        if len(event.tightLeps) == 0: return False
        if event.tightLeps[0].pt < 25: return False
        if len(event.selPhotons) == 0: return False
        return True
