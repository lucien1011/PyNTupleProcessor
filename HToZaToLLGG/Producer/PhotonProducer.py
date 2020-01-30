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
        event.selPhotons = [ph for ph in photons if sphf.idSphection(ph) and sphf.isoSphection(ph)]
        return True
