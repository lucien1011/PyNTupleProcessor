from Core.Module import Module
import ROOT as r
from ROOT import TLorentzVector

class EventSkimmer(Module):
    def __init__(self,name):
        super(EventSkimmer,self).__init__(name)

    def analyze(self,event):
        Lep1, Lep2, Lep3, Met = TLorentzVector(), TLorentzVector(), TLorentzVector(), TLorentzVector(),
        Lep1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
        Lep2.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
        Lep3.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
        Met.SetPtEtaPhiM(event.met[0],0,event.met_phi[0],0)
        vec = Lep1 + Lep2 + Lep3 + Met
        event.mt = vec.Mt()
        P1 = Lep1 + Lep2
        P2 = P1
        if event.idL1[0] > 0 and event.idL3[0] < 0:
            P2 = Lep1 + Lep3
        if event.idL1[0] < 0 and event.idL3[0] > 0:
            P2 = Lep1 + Lep3
        if event.idL2[0] > 0 and event.idL3[0] < 0:
            P2 = Lep2 + Lep3
        if event.idL2[0] < 0 and event.idL3[0] > 0:
            P2 = Lep2 + Lep3
        event.twolpt = P1.Pt()
        event.mass1  = P1.M()
        event.mass2  = P2.M()
        if event.mass1 <= 5 or event.mass2 <= 5:
            return False
        if 8 < event.mass1 <  12 or 8 < event.mass2 < 12 or 80 < event.mass1 < 100 or 80 < event.mass2 < 100:
            return False
        #if not(event.mass1 > 86 and (event.mass1 < 96)):
            #return False
        #if event.mass1 > 86 and event.mass1 < 96:
            #return False
        #if 8 < event.mass1 < 12:
            #return False
        #if event.met[0] <= 100:
            #return False
        return True
