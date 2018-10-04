from Core.Module import Module
from Core.Collection import Collection

class PhotonProducer(Module):
    def analyze(self,event):
        event.photons = Collection(event,"PhoGood")
        event.selPhotons = [p for p in event.photons if self.isTightPho(p)]
        event.selPhotons.sort(key=lambda x: x.pt,reverse=True)

        return True

    @staticmethod
    def isTightPho(pho):
        return pho.idCutBased == 3 and pho.pt > 40. and abs(pho.eta) < 2.5
