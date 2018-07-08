from Core.Module import Module
from Core.Collection import Collection 

class CollectionProducer(Module):
    def analyze(self,event):
        event.leps = [lep for lep in Collection(event,"lep") if ((abs(lep.eta) < 2.5 and abs(lep.id) == 11 and lep.pt > 7) or (abs(lep.eta) < 2.4 and abs(lep.id) == 13 and lep.pt > 5)) and lep.RelIso < 0.35]
        event.leps.sort(key=lambda x: x.pt,reverse=True)
        return True
