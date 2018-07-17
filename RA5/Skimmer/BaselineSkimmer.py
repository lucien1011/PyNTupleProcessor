from Core.Module import Module 
from RA5.LeptonJetRecleaner.Algo import passMllVeto

class BaselineSkimmer(Module):
    def analyze(self,event):
        if event.ret["htJet40j_Mini"] < 80.: return False
        if event.ret["nJet40_Mini"] < 2: return False
        
        nSSLepPlus = 0
        nSSLepMinus = 0
        for l in event.tightLeps:
            if l.pdgId == 11 or l.pdgId == 13: nSSLepPlus += 1
            if l.pdgId == -11 or l.pdgId == -13: nSSLepMinus += 1
        if nSSLepPlus != 2 and nSSLepMinus != 2: return False
        if not self.passMllTL(event.looseLeps,event.tightLeps,[0.,12.],[76.,106.]): return False
        if (event.tightLeps[0].p4()+event.tightLeps[1].p4()).M() < 8.: return False
        return True
    
    def passMllTL(self,lepsl, lepst , mZ1Ranges, mZ2Ranges):
        pairs = []
        for l1 in lepst:
            for l2 in lepsl:
                if l2 == l1: continue
                if not passMllVeto(l1,l2,mZ1Ranges[0],mZ1Ranges[1],True): return False
                if not passMllVeto(l1,l2,mZ2Ranges[0],mZ2Ranges[1],True): return False
        return True
