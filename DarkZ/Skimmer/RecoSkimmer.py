from Core.Module import Module
from Core.Collection import Collection 

from DarkZ.Common.HZZAlgo import HZZAlgo

class RecoSkimmer(Module):
    def __init__(self,name):
        self.name = name
        self.HZZAlgo = HZZAlgo()

    def analyze(self,event):
        #event.leps = [lep for lep in Collection(event,"lep") if ((abs(lep.eta) < 2.5 and abs(lep.id) == 11 and lep.pt > 7) or (abs(lep.eta) < 2.4 and abs(lep.id) == 13 and lep.pt > 5)) and lep.RelIso < 0.35]
        event.leps = [lep for lep in Collection(event,"lepFSR") if ((abs(lep.eta) < 2.5 and abs(lep.id) == 11 and lep.pt > 7) or (abs(lep.eta) < 2.4 and abs(lep.id) == 13 and lep.pt > 5)) and lep.RelIso < 0.35]
        event.leps.sort(key=lambda x: x.pt,reverse=True)

        if len(event.leps) < 4: return False
        
        if event.leps[0].pt < 20: return False
        if event.leps[1].pt < 10: return False

        if not self.OSSFLeptonPairs(event.leps): return False
        event.ZCandidates = self.HZZAlgo.makeZCandidatesFromCollection(event.leps)
        Z1,Z2,passZ1Z2 = self.HZZAlgo.makeZ1Z2(event.ZCandidates,[40.,120.],[12.,120.]) 
        #if Z1.vec.M() < 40 or Z1.vec.M() > 120: return False
        #if Z2.vec.M() < 12 or Z2.vec.M() > 120: return False
        event.Z1 = Z1
        event.Z2 = Z2
        if not passZ1Z2: return False

        lep_vec_list = [Z1.lep1.vec,Z1.lep2.vec,Z2.lep1.vec,Z2.lep2.vec]
        deltaRs = []
        for i,vec1 in enumerate(lep_vec_list):
            for j,vec2 in enumerate(lep_vec_list):
                if i >= j: continue
                deltaRs.append(vec1.DeltaR(vec2))
        if min(deltaRs) < 0.02: return False
        
        hvec = Z1.vec + Z2.vec
        event.hmass = hvec.M()
        if event.hmass < 105 or event.hmass > 140: return False
        
        #return event.passedFiducialSelection[0]
        return True

    def OSSFLeptonPairs(self,leps):
        Nmm = 0
        Nmp = 0
        Nem = 0
        Nep = 0
        lepids = [lep.id for lep in leps]
        for lep_id in lepids:
            if lep_id == -13:
                Nmm += 1
            elif lep_id == 13:
                Nmp += 1
            elif lep_id == -11:
                Nem += 1
            elif lep_id == 11:
                Nep += 1
        return (Nmm >= 2 and Nmp >= 2) or (Nem >=2 and Nep >= 2) or (Nmm > 0 and Nmp > 0 and Nem > 0 and Nep > 0)


