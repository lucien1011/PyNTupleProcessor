from Core.Module import Module
import ROOT

muonMass = 0.
zMass = 91.1876
class ZabVetoSkimmer(Module):
    def analyze(self,event):
        event.vecL1 = ROOT.TLorentzVector()
        event.vecL1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],muonMass)

        event.vecL2 = ROOT.TLorentzVector()
        event.vecL2.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],muonMass)
        
        event.vecL3 = ROOT.TLorentzVector()
        event.vecL3.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],muonMass)
        
        event.vecL4 = ROOT.TLorentzVector()
        event.vecL4.SetPtEtaPhiM(event.pTL4[0],event.etaL4[0],event.phiL4[0],muonMass)

        if event.idL1[0]*event.idL3[0] < 0:
            event.vecZi = event.vecL1 + event.vecL3
            event.vecZj = event.vecL2 + event.vecL4
        else:
            event.vecZi = event.vecL1 + event.vecL4
            event.vecZj = event.vecL2 + event.vecL3
        if abs(event.vecZi.M()-zMass) < abs(event.vecZj.M()-zMass):
            event.vecZa = event.vecZi
            event.vecZb = event.vecZj
        else:
            event.vecZa = event.vecZj
            event.vecZb = event.vecZi
        if (abs(event.idL1[0]) == 11 and abs(event.idL2[0]) == 11 and abs(event.idL3[0]) == 11 and abs(event.idL4[0]) == 11) or (abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13):
            return abs(event.vecZa.M()-zMass) > 7.5
        else:
            return True
