import ROOT

from Core.Module import Module
from Core.Collection import Collection

class PhotonProducer(Module):
    def __init__(self,name,idSelection,isoSelection,otherSelection):
        super(PhotonProducer,self).__init__(name)
        self.idSelection = idSelection
        self.isoSelection = isoSelection
        self.otherSelection = otherSelection

    def analyze(self,event):
        photons = Collection(event,"Photon")
        event.selPhotons = [ph for ph in photons if self.idSelection(ph) and self.isoSelection(ph) and self.otherSelection(ph)]
        return True

    def end(self):
        self.idSelection.end()
        self.isoSelection.end()
        self.otherSelection.end()
