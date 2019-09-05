from Core.Module import Module
import ROOT as r
from ROOT import TLorentzVector

class EventSkimmer(Module):
    def __init__(self,name):
        super(EventSkimmer,self).__init__(name)

    def analyze(self,event):
        temp1 = event.pTL1[0]
        temp2 = event.pTL1[0]
        event.Lep1, event.Lep2, event.Lep3, event.Met = TLorentzVector(), TLorentzVector(), TLorentzVector(), TLorentzVector(),
        event.Met.SetPtEtaPhiM(event.met[0],0,event.met_phi[0],0)
        if event.pTL3[0] > event.pTL1[0]:
            event.Lep1.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
            event.Lep2.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
            event.Lep3.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
        if event.pTL1[0] > event.pTL3[0] > event.pTL2[0]:
            event.Lep1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
            event.Lep2.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
            event.Lep3.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
        if event.pTL3[0] < event.pTL2[0]:
            event.Lep1.SetPtEtaPhiM(event.pTL1[0],event.etaL1[0],event.phiL1[0],event.massL1[0])
            event.Lep2.SetPtEtaPhiM(event.pTL2[0],event.etaL2[0],event.phiL2[0],event.massL2[0])
            event.Lep3.SetPtEtaPhiM(event.pTL3[0],event.etaL3[0],event.phiL3[0],event.massL3[0])
        vec = event.Lep1 + event.Lep2 + event.Lep3 + event.Met
        event.mt = vec.Mt()
        if event.pTL3[0] > event.pTL1[0]:
            if event.idL3[0] > 0 and event.idL1[0] > 0:
                P1 = event.Lep1 + event.Lep3
                P2 = event.Lep2 + event.Lep3
            if event.idL3[0] < 0 and event.idL1[0] < 0:
                P1 = event.Lep1 + event.Lep3
                P2 = event.Lep2 + event.Lep3
            if event.idL3[0] > 0 and event.idL1[0] < 0:
                P1 = event.Lep1 + event.Lep2
                if event.idL2[0] < 0:
                    P2 = event.Lep1 + event.Lep3
                else:
                    P2 = event.Lep2 + event.Lep3
            if event.idL3[0] < 0 and event.idL1[0] > 0:
                P1 = event.Lep1 + event.Lep2
                if event.idL2[0] > 0:
                    P2 = event.Lep1 + event.Lep3
                else:
                    P2 = event.Lep2 + event.Lep3
        if event.pTL1[0] > event.pTL3[0] > event.pTL2[0]:
            if event.idL1[0] > 0 and event.idL3[0] > 0:
                P1 = event.Lep1 + event.Lep3
                P2 = event.Lep2 + event.Lep3
            if event.idL1[0] < 0 and event.idL3[0] < 0:
                P1 = event.Lep1 + event.Lep3
                P2 = event.Lep2 + event.Lep3
            if event.idL1[0] > 0 and event.idL3[0] < 0:
                P1 = event.Lep1 + event.Lep2
                if event.idL2[0] < 0:
                    P2 = event.Lep1 + event.Lep3
                else:
                    P2 = event.Lep2 + event.Lep3
            if event.idL1[0] < 0 and event.idL3[0] > 0:
                P1 = event.Lep1 + event.Lep2
                if event.idL2[0] > 0:
                    P2 = event.Lep1 + event.Lep3
                else:
                    P2 = event.Lep2 + event.Lep3
        if event.pTL3[0] < event.pTL2[0]:
            if event.idL1[0] > 0 and event.idL2[0] > 0:
                P1 = event.Lep1 + event.Lep3
                P2 = event.Lep2 + event.Lep3
            if event.idL1[0] < 0 and event.idL2[0] < 0:
                P1 = event.Lep1 + event.Lep3
                P2 = event.Lep2 + event.Lep3
            if event.idL1[0] > 0 and event.idL2[0] < 0:
                P1 = event.Lep1 + event.Lep2
                if event.idL3[0] < 0:
                    P2 = event.Lep1 + event.Lep3
                else:
                    P2 = event.Lep2 + event.Lep3
            if event.idL1[0] < 0 and event.idL2[0] > 0:
                P1 = event.Lep1 + event.Lep2
                if event.idL3[0] > 0:
                    P2 = event.Lep1 + event.Lep3
                else:
                    P2 = event.Lep2 + event.Lep3
        event.twolpt = P1.Pt()
        event.mass1  = P1.M()
        event.mass2  = P2.M()
        #if event.mass1 <= 5 or event.mass2 <= 5:
            #return False
        if 8 < event.mass1 <  12 or 8 < event.mass2 < 12 or 80 < event.mass1 < 100 or 80 < event.mass2 < 100:
            return False
        #if event.MomIdL1[0] != 999888 and event.MomIdL3[0] != 999888 and event.MomIdL3[0] != 999888:
            #print event.MomIdL1[0], "   ",event.MomIdL2[0], "   " , event.MomIdL3[0]
        #if not(event.mass1 > 86 and (event.mass1 < 96)):
            #return False
        #if event.mass1 > 86 and event.mass1 < 96:
            #return False
        #if 8 < event.mass1 < 12:
            #return False
        #if event.met[0] <= 100:
            #return False
        return True
