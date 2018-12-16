from Core.Module import Module
from Core.Collection import Collection

class LeptonProducer(Module):
    def analyze(self,event):
        event.goodLeps = [l for l in Collection(event,"LepGood")]
        event.looseLeps = []
        event.tightLeps = []
        event.cleanLeps = []
        for il,l in enumerate(event.goodLeps):
            if l.isTight: event.tightLeps.append(l)
            if l.isLoose and not l.isTight: event.looseLeps.append(l)
            if l.isCleaning and not l.isTight: event.cleanLeps.append(l)
        return True
