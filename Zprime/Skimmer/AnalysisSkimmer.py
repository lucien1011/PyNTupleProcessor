from __future__ import division
from Core.Module import Module
from Utils.DeltaR import deltaR

class AnalysisSkimmer(Module):
    def __init__(self,name,cutflow="Zprime-SR"):
        super(AnalysisSkimmer,self).__init__(name)
        self.cutflow = cutflow

    def analyze(self,event):
        if self.cutflow == "Zprime-SR":
            #if event.mass4l[0] < 80. or event.mass4l[0] > 100.: return False
            #if event.mass4l[0] < 100.: return False
            #if event.mass4l[0] > 120.: return False
            #if event.mass4l[0] < 118. or event.mass4l[0] > 130.: return False
            if event.massZ1[0] < 12. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 1. or event.massZ2[0] > 120.: return False
            if "ZPlusX" not in self.dataset.name and not event.passedFullSelection[0]: return False
            #if event.nZXCRFailedLeptons[0] != 1: return False
            #if event.nZXCRFailedLeptons[0] != 2: return False
            zplep1 = -1
            zplep2 = -1
            if "zpToMuMu" in self.dataset.name:
                for i in range(0,int(event.GENlep_id.size())):
                    if abs(event.GENlep_id[i]) == 13 and event.GENlep_MomId[i] == 999888:
                        if zplep1 == -1:
                            zplep1 = i
                        elif zplep2 == -1:
                            zplep2 = i
                        else:
                            break
                if zplep1 != -1 and zplep2 != -1:
                    event.deltaRGENZpLep = deltaR(event.GENlep_eta[zplep1],event.GENlep_phi[zplep1],event.GENlep_eta[zplep2],event.GENlep_phi[zplep2])
            return True
        return False
