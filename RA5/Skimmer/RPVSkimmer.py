from Core.Module import Module

class RPVSkimmer(Module):
    def analyze(self,event):
        if event.htJet40[0] < 300.: return False
        #return event.met_pt[0] > 0. and event.met_pt[0] < 50.
        return True
