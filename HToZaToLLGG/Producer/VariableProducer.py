import ROOT

from Core.Module import Module
from Core.Collection import Collection

class VariableProducer(Module):
    def analyze(self,event):
        return True
