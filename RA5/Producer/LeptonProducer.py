from Core.Module import Module
from Core.Collection import Collection

class LeptonJetProducer(Module):
    def analyze(self,event):
        event.goodLeps = [l for l in Collection(event,"LepGood")]
        event.looseLeps = []
        event.tightLeps = []
        for il,l in enumerate(event.goodLeps):
            if l.isTight: event.tightLeps.append(l)
            if l.isLoose: event.looseLeps.append(l)
        return True
