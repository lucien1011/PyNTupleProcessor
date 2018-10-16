from Core.Module import Module 
from RA5.LeptonJetRecleaner.Algo import passMllVeto

class TightLooseSkimmer(Module):
    def analyze(self,event):
        if event.htJet40[0] < 80: return False
        if event.nJetRA540[0] < 2: return False

        event.firstLep = event.tightLeps[0]
        if event.firstLep.pt < 25: return False

        event.found2nd = False
        for l in event.cleanLeps:
            if l.pt < 10: continue
            if l.charge == event.firstLep.charge:
                event.found2nd = True
                event.secondLep = l
        
        if not event.found2nd: return False
        if event.secondLep.pt < 25: return False

        #if event.met_pt[0] < 50.: return False
        #if event.met_pt[0] > 50.: return False
        #if event.selJets[0].chHEF < 0.1: return False
        
        if not self.passMllTL(event.looseLeps,event.tightLeps,[0.,12.],[76.,106.]): return False 
        return True
    
    def passMllTL(self,lepsl, lepst , mZ1Ranges, mZ2Ranges):
        pairs = []
        for l1 in lepst:
            for l2 in lepsl:
                if l2 == l1: continue
                if not passMllVeto(l1,l2,mZ1Ranges[0],mZ1Ranges[1],True): return False
                if not passMllVeto(l1,l2,mZ2Ranges[0],mZ2Ranges[1],True): return False
        return True
