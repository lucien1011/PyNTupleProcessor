from Core.Module import Module
from Core.Collection import Collection 

class NLeptonSkimmer(Module):
    def analyze(self,event):
        if len(event.leps) < 4: return False
        return True
