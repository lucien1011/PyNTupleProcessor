from Core.Module import Module
from Utils.DeltaR import deltaR

muonMass = 0.

class VariableProducer(Module):
    def analyze(self,event):
        event.deltaRL12 = deltaR(event.etaL1[0],event.phiL1[0],event.etaL2[0],event.phiL2[0])
        event.vecL1 = ROOT.TLorentzVector()
        event.vecL1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],muonMass)

        event.vecL2 = ROOT.TLorentzVector()
        event.vecL2.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],muonMass)
        
        event.vecL3 = ROOT.TLorentzVector()
        event.vecL3.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],muonMass)
        
        event.vecL4 = ROOT.TLorentzVector()
        event.vecL4.SetPtEtaPhiM(event.pTL4[0],event.etaL4[0],event.phiL4[0],muonMass)

        event.vecZ1 = event.vecL1 + event.vecL2
        event.vecZ2 = event.vecL3 + event.vecL4

        return True
