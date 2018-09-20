from Core.Module import Module

class RPVSkimmer(Module):
    def analyze(self,event):
        #return event.met_pt[0] > 0. and event.met_pt[0] < 50.
        return True
