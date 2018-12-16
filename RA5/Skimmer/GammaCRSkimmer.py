from Core.Module import Module
from Utils.DeltaR import deltaR

class GammaCRSkimmer(Module):
    def analyze(self,event):
        # same as skim tree selection, redundant if running on skim tree
        if len(event.tightLeps) == 0: return False
        if event.tightLeps[0].pt < 25: return False
        if len(event.selPhotons) == 0: return False

        if len(event.tightLeps) != 1: return False
        event.firstLep = event.tightLeps[0]
        deltaRList = [deltaR(event.tightLeps[0].eta,event.tightLeps[0].phi,pho.eta,pho.phi) for pho in event.selPhotons ]
        if min(deltaRList) < 0.3: return False
        return True

class GammaCRTreeSkimmer(Module):
    def analyze(self,event):
        if len(event.tightLeps) == 0: return False
        if event.tightLeps[0].pt < 25: return False
        if len(event.selPhotons) == 0: return False
        return True
