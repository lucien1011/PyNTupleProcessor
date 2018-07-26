from Core.Module import Module
from Core.Collection import Collection 

from DarkZ.Common.HZZAlgo import HZZAlgo

class RecoSkimmer(Module):
    def __init__(self,name):
        self.name = name
        self.HZZAlgo = HZZAlgo()
        self.elPtCut = 7.0
        self.elEtaCut = 2.5
        self.muPtCut = 5.0
        self.muEtaCut = 2.4
        self.lepRelIso = 0.35
        self.nLep = 4
        self.leadingPtCut = 20
        self.subleadingPtCut = 10
        self.Z1MassRange = [40.,120.]
        self.Z2MassRange = [12.,120.]
        self.deltaRCut = 0.02
        self.m4lRange = [105.,140.]

    def analyze(self,event):
        event.leps = [lep for lep in Collection(event,"lep") if ((abs(lep.eta) < self.elEtaCut and abs(lep.id) == 11 and lep.pt > self.elPtCut) or (abs(lep.eta) < self.muEtaCut and abs(lep.id) == 13 and lep.pt > self.muPtCut)) and lep.RelIso < self.lepRelIso]
        #event.leps = [lep for lep in Collection(event,"lepFSR") if ((abs(lep.eta) < 2.5 and abs(lep.id) == 11 and lep.pt > 7) or (abs(lep.eta) < 2.4 and abs(lep.id) == 13 and lep.pt > 5)) and lep.RelIso < 0.35]
        event.leps.sort(key=lambda x: x.pt,reverse=True)

# Check for Nlep >= 4:
        if len(event.leps) < self.nLep: return False
        
        if event.leps[0].pt < self.leadingPtCut: return False
        if event.leps[1].pt < self.subleadingPtCut: return False

        if not self.OSSFLeptonPairs(event.leps): return False
        event.ZCandidates = self.HZZAlgo.makeZCandidatesFromCollection(event.leps,useFSR=True)
        Z1,Z2,passZ1Z2 = self.HZZAlgo.makeZ1Z2(event.ZCandidates,self.Z1MassRange,self.Z2MassRange) 
        #if Z1.vec.M() < 40 or Z1.vec.M() > 120: return False
        #if Z2.vec.M() < 12 or Z2.vec.M() > 120: return False
        event.Z1 = Z1
        event.Z2 = Z2
        if not passZ1Z2: return False

	# Make list of the four leptons which come from the Z bosons.
	# Generally, lep1 and lep2 come from Z1; lep3 and lep4 come from Z2
        lep_vec_list = [Z1.lep1.vec, Z1.lep2.vec, Z2.lep1.vec, Z2.lep2.vec]
        deltaRs = []
        for i,vec1 in enumerate(lep_vec_list):
            for j,vec2 in enumerate(lep_vec_list):
                if i >= j: continue
                deltaRs.append(vec1.DeltaR(vec2))
        if min(deltaRs) < self.deltaRCut: return False
        
        hvec = Z1.vec + Z2.vec
        event.hmass = hvec.M()
        if event.hmass < self.m4lRange[0] or event.hmass > self.m4lRange[1]: return False
        
        #return event.passedFiducialSelection[0]
        return True

    def OSSFLeptonPairs(self,leps):
	# mm = muon_minus (13), mp = muon_plus (-13), em = electron_minus (11), ep = electron_plus (-11)
        Nmm = 0
        Nmp = 0
        Nem = 0
        Nep = 0
        lepids = [lep.id for lep in leps]
        for lep_id in lepids:
            if lep_id == 13:
                Nmm += 1
            elif lep_id == -13:
                Nmp += 1
            elif lep_id == 11:
                Nem += 1
            elif lep_id == -11:
                Nep += 1
	# Require at least 4 leptons
        return (Nmm >= 2 and Nmp >= 2) or (Nem >= 2 and Nep >= 2) or (Nmm > 0 and Nmp > 0 and Nem > 0 and Nep > 0)


