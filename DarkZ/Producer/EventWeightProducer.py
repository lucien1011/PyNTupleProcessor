
from Core.Module import Module

class EventWeightProducer(Module):
    def analyze(self,event):
        event.weight = 1.
        if self.dataset.isMC:
            event.weight *= event.dataMCWeight[0]
            event.weight *= event.pileupWeight[0]
            event.weight *= event.genWeight[0]
            xs = event.crossSection[0] if "ggHZZd" not in self.dataset.name else self.dataset.xs
            event.weight *= xs*35.9*1000/self.dataset.sumw
        return True
