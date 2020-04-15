from Core.Module import Module
from Core.Collection import Collection

var_lep_str = "lep"

class ZCandProducer(Module):
    def analyze(self,event):
        event.leptons = [l for l in Collection(event,var_lep_str)]
        print [l.matchedR03_MomId,matchedR03_MomMomId for l in event.leptons]
        return True
