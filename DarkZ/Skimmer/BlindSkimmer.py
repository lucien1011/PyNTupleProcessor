from Core.Module import Module

class BlindSkimmer(Module):
    def analyze(self,event):
        if self.dataset.parent.isData: return event.Z2mass > 12.
        return True
