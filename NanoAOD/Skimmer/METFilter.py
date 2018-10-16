from Core.Module import Module

flags = [
        "Flag_HBHENoiseFilter",
        "Flag_HBHENoiseIsoFilter",
        "Flag_EcalDeadCellTriggerPrimitiveFilter",
        "Flag_goodVertices",
        "Flag_eeBadScFilter",
        # Reconstruction filters:
        "Flag_muonBadTrackFilter",
        "Flag_chargedHadronTrackResolutionFilter",
        "Flag_globalTightHalo2016Filter",
        # Moriond17 bad muons (temporary recipe from https://hypernews.cern.ch/HyperNews/CMS/get/physics-validation/2786.html)
        #"Flag_badMuonMoriond2017",
        #"Flag_badCloneMuonMoriond2017",
        ]

class METFilter(Module):
    def __init__(self,name,flags=flags):
        super(METFilter,self).__init__(name)
        self.flags = flags

    def analyze(self,event):
        #if self.dataset.isMC: return True
        for flag in self.flags:
            if not getattr(event,flag)[0]: return False
        return True
