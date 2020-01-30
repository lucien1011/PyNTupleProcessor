import ROOT

from Core.Module import Module
from Core.Collection import Collection

class PhotonProducer(Module):
    def __init__(self,name,idSelection,isoSelection):
        super(PhotonProducer,self).__init__(name)
        self.idSelection = idSelection
        self.isoSelection = isoSelection

    def analyze(self,event):
        photons = Collection(event,"Photon")
        event.selPhotons = [ph for ph in photons if self.idSelection(ph) and self.isoSelection(ph)]
        return True

    def end(self):
        self.idSelection.end()
        self.isoSelection.end()
