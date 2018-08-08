from Core.Module import Module

class DataMCWeighter(Module):
    def analyze(self,event):
        if self.dataset.isMC and not self.dataset.skipWeight:
            event.weight *= event.dataMCWeight[0]*event.pileupWeight[0]
        return True
