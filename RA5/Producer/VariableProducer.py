from Core.Module import Module
from Utils.MiscVar import mtFunc

class VariableProducer(Module):
    def analyze(self,event):

        event.mtmin = min([mtFunc(event.firstLep.pt,event.firstLep.phi,event.met_pt[0],event.met_phi[0]),mtFunc(event.secondLep.pt,event.secondLep.phi,event.met_pt[0],event.met_phi[0]),])
        return True
