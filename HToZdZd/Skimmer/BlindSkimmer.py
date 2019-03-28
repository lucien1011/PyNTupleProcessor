from Core.Module import Module

### All modules must return True for the event to pass selection criteria ###

class BlindSkimmer(Module):
    def analyze(self,event):
        if self.dataset.parent.isData or self.dataset.parent.isMC: return not (event.mass4l[0] > 118. and event.mass4l[0] < 130.)
        return True
