from Core.Module import Module
from Utils.DeltaR import deltaR,deltaPhi
from Physics.Muon import muon_mass
from Physics.Electron import electron_mass

import ROOT

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

        event.phiL21 = deltaPhi(event.phiL2[0],event.phiL1[0])
        event.phiL31 = deltaPhi(event.phiL3[0],event.phiL1[0])
        event.phiL41 = deltaPhi(event.phiL4[0],event.phiL1[0])
        
        event.vecL1 = ROOT.TLorentzVector()
        event.vecL1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],self.get_mass(event.idL1[0]))

        event.vecL2 = ROOT.TLorentzVector()
        event.vecL2.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],self.get_mass(event.idL2[0]))
        
        event.vecL3 = ROOT.TLorentzVector()
        event.vecL3.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],self.get_mass(event.idL3[0]))
        
        event.vecL4 = ROOT.TLorentzVector()
        event.vecL4.SetPtEtaPhiM(event.pTL4[0],event.etaL4[0],event.phiL4[0],self.get_mass(event.idL4[0]))

        #if event.minDeltaRL < 0.3: return False
        #if event.minDeltaRL < 0.6: return False
        return True

    def get_mass(self,lepton_id):
        if abs(lepton_id) == 11:
            return electron_mass
        elif abs(lepton_id) == 13:
            return muon_mass
