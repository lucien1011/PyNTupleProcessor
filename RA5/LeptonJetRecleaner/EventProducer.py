from Core.Module import Module
from Core.Collection import Collection
from RA5.LeptonJetRecleaner.LeptonDict import leptonAlgoDict

class LeptonJetProducer(Module):
    def __init__(self,name,algoStr):
        self.name = name
        self.algoStr = algoStr

    def analyze(self,event):
        event.ret = leptonAlgoDict[self.algoStr](event)

        event.goodLeps = [l for l in Collection(event,"LepGood")]
        event.looseLeps = []
        event.tightLeps = []
        for il,l in enumerate(event.goodLeps):
            if event.ret["LepGood_isTight_Mini"][il]: event.tightLeps.append(l)
            if event.ret["LepGood_isLoose_Mini"][il]: event.looseLeps.append(l)
        return True
