from Core.Module import Module 
from RA5.LeptonJetRecleaner.Algo import passMllVeto
from Utils.MiscVar import mtFunc

class BaselineSkimmer(Module):
    def analyze(self,event):
        #if event.ret["htJet40j_Mini"] < 80.: return False
        #if event.ret["nJet40_Mini"] < 2: return False
        if event.htJet40[0] < 80: return False
        if event.nJetRA540[0] < 2: return False

        event.firstLep = event.tightLeps[0]
        event.found2nd = False
        for l in event.tightLeps[1:]:
            if l.charge == event.firstLep.charge:
                event.found2nd = True
                secondLep = l
        
        if len(event.tightLeps) < 2: return False
        if not event.found2nd: return False
        event.secondLep = secondLep
        
        if not self.passMllTL(event.looseLeps,event.tightLeps,[0.,12.],[76.,106.]): return False
        
        mllList = []
        nTightLep = len(event.tightLeps)
        for il in range(0,nTightLep-1):
            lep1 = event.tightLeps[il]
            for jl in range(il+1,len(event.tightLeps)):
                lep2 = event.tightLeps[jl]
                lep12Vec = lep1.p4()+lep2.p4()
                mll = lep12Vec.M()
                mllList.append(mll)

        if min(mllList) < 8.: return False

        mt = min([mtFunc(event.firstLep.pt,event.firstLep.phi,event.met_pt[0],event.met_phi[0]),mtFunc(event.secondLep.pt,event.secondLep.phi,event.met_pt[0],event.met_phi[0]),])
        event.mtmin = mt
         
        return True
    
    def passMllTL(self,lepsl, lepst , mZ1Ranges, mZ2Ranges):
        pairs = []
        for l1 in lepst:
            for l2 in lepsl:
                if l2 == l1: continue
                if not passMllVeto(l1,l2,mZ1Ranges[0],mZ1Ranges[1],True): return False
                if not passMllVeto(l1,l2,mZ2Ranges[0],mZ2Ranges[1],True): return False
        return True

class NJetSkimmer(Module):
    def analyze(self,event):
        if event.ret["nJet40_Mini"] < 2: return False
        return True

class TreeSkimmer(Module):
    def analyze(self,event):
        if event.ret["nJet40_Mini"] < 2: return False
        if len(event.tightLeps) < 1: return False
        return True

