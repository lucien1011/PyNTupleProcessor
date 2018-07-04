from Core.Module import Module

import ROOT

class HZZSkimmer(Module):
    def __init__(self,name):
        super(HZZSkimmer,self).__init__(name)
        self.Zmass = 91.1876
        self.isoCutEl = 0.35
        self.isoCutMu = 0.35
        self.leadingLepPtCut = 20.0
        self.subleadingLepPtCut = 10.0
        self.deltaRCut = 0.02
        self.mllCut = 4.
        self.mZ1Range = [80.,100.]
        self.mZ2Range = [4.,120.]
        self.m4lLowCut = 115.

    def analyze(self,event):
        if not self.OSSFLeptonPairs(event): return False
        ZCandidates = self.makeZCandidates(event)
        #HiggsCandidates = self.makeHiggsCandidates(ZCandidates,event)
        return True

    def OSSFLeptonPairs(self,event):
        Nmm = 0
        Nmp = 0
        Nem = 0
        Nep = 0
        for lep_id in event.lep_id:
            if lep_id == -13:
                Nmm += 1
            elif lep_id == 13:
                Nmp += 1
            elif lep_id == -11:
                Nem += 1
            elif lep_id == 11:
                Nep += 1
        return (Nmm >= 2 and Nmp >= 2) or (Nem >=2 and Nep >= 2) or (Nmm > 0 and Nmp > 0 and Nem > 0 and Nep > 0)
