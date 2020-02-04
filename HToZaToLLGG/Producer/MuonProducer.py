import ROOT

from Core.Module import Module
from Core.Collection import Collection

class MuonProducer(Module):
    def __init__(self,name,idSelection,isoSelection,otherSelection):
        super(MuonProducer,self).__init__(name)
        self.idSelection = idSelection
        self.isoSelection = isoSelection
        self.otherSelection = otherSelection

    def analyze(self,event):
        muons = Collection(event,"Muon")
        event.selMuons = [mu for mu in muons if self.idSelection(mu) and self.isoSelection(mu) and self.otherSelection(mu)]
        return True

    def end(self):
        self.idSelection.end()
        self.isoSelection.end()
        self.otherSelection.end()
