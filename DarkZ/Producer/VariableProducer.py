from Core.Module import Module
from Utils.DeltaR import deltaR

class VariableProducer(Module):
    def analyze(self,event):
        event.deltaRL12 = deltaR(event.etaL1[0],event.phiL1[0],event.etaL2[0],event.phiL2[0])
        event.deltaRL13 = deltaR(event.etaL1[0],event.phiL1[0],event.etaL3[0],event.phiL3[0])
        event.deltaRL14 = deltaR(event.etaL1[0],event.phiL1[0],event.etaL4[0],event.phiL4[0])
        event.deltaRL23 = deltaR(event.etaL2[0],event.phiL2[0],event.etaL3[0],event.phiL3[0])
        event.deltaRL24 = deltaR(event.etaL2[0],event.phiL2[0],event.etaL4[0],event.phiL4[0])
        event.deltaRL34 = deltaR(event.etaL3[0],event.phiL3[0],event.etaL4[0],event.phiL4[0])
        event.minDeltaRL = min([event.deltaRL12, 
                               event.deltaRL13,
                               event.deltaRL14,
                               event.deltaRL23,
                               event.deltaRL24,
                               event.deltaRL34,])
        #if event.minDeltaRL < 0.3: return False
        #if event.minDeltaRL < 0.6: return False
        return True
