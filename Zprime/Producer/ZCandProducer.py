from Core.Module import Module
from Core.Collection import Collection

from Zprime.Physics.Zp import Zp,Z

var_lep_str = "lep"

class ZCandProducer(Module):
    def analyze(self,event):
        event.leptons = [l for l in Collection(event,var_lep_str)]
        event.leptons_Zp = [l for l in event.leptons if abs(l.matchedR03_MomId) == Zp.pdgId]
        event.leptons_nonZp = [l for l in event.leptons if abs(l.matchedR03_MomId) != Zp.pdgId]
        event.leptons_matched = event.leptons_Zp if self.dataset.isZp else event.leptons_nonZp
        return True
