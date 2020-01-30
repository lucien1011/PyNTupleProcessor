import ROOT

from Core.Module import Module
from Core.Collection import Collection

class SRSkimmer(Module):
    def analyze(self,event):
        if len(event.selElectrons) != 2: return False
        if event.selElectrons[0].charge[0] == event.selElectrons[1].charge[0]: return False
        if len(event.selPhotons) != 2: return False
        return True
