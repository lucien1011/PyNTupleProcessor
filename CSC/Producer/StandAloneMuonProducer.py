from Core.Module import Module
from Core.Collection import Collection

class StandAloneMuonProducer(Module):
    def analyze(self,event):
        event.standAloneMuons = [m for m in Collection(event,"muons") if m.isStandAloneMuon ]
        return True
