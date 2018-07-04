from Core.Module import Module

import ROOT

class OSSFLeptonSkimmer(Module):
    def __init__(self,name):
        super(OSSFLeptonSkimmer,self).__init__(name)

    def analyze(self,event):
        if not self.OSSFLeptonPairs(event): return False
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
