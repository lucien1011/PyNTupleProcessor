from Core.Module import Module

class BlindSkimmer(Module):
    def analyze(self,event):
        if self.dataset.parent.isData: return event.massZ2[0] > 12.
        return True
