from Core.Module import Module

class BlindSkimmer(Module):
    def analyze(self,event):
        if self.dataset.parent.isData: return not (event.mass4l[0] > 108. and event.mass4l[0] < 130.)
        return True
