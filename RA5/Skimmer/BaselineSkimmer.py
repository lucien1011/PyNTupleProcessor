from Core.Module import Module 

class BaselineSkimmer(Module):
    def analyze(self,event):
        #if event.minMllSFOS_Mini[0] < 12.: return False
        #if event.minMllSFOS_Mini[0] > 76. and event.minMllSFOS_Mini[0] < 106.: return False
        if event.htJet40j_Mini[0] < 80.: return False
        if event.met_pt[0] < 50.: return False
        if event.nJet40_Mini[0] < 2: return False
        return True
