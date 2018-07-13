from Core.Module import Module

class FourLeptonMassSkimmer(Module):
    def analyze(self,event):        
        hvec = event.Z1.vec + event.Z2.vec
        event.hmass = hvec.M()
        if event.hmass < 105 or event.hmass > 140: return False
        return True
