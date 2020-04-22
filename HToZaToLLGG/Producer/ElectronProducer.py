import ROOT

from Core.Module import Module
from Core.Collection import Collection

class ElectronProducer(Module):
    def __init__(self,name,idSelection,isoSelection,otherSelection):
        super(ElectronProducer,self).__init__(name)
        self.idSelection = idSelection
        self.isoSelection = isoSelection
        self.otherSelection = otherSelection

    def analyze(self,event):
        electrons = Collection(event,"Electron")
        event.selElectrons = [el for el in electrons if self.idSelection(el) and self.isoSelection(el) and self.otherSelection(el)]
        return True

    def end(self):
        self.idSelection.end()
        self.isoSelection.end()
        self.otherSelection.end()
