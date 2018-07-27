from Core.Module import Module

class DataMCWeighter(Module):
    def analyze(self,event):
        if self.dataset.parent.isMC:
            event.weight *= event.dataMCWeight[0]
        return True
