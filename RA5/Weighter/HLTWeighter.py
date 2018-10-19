from Core.Module import Module
import ROOT

class HLTWeighter(Module):
    def __init__(self,name,cutflow="SR"):
        super(HLTWeighter,self).__init__(name)
        self.cutflow = cutflow

    def begin(self):
        ROOT.gSystem.Load("Library/TriggerSF_Moriond2017_cxx.so")
        
    def analyze(self,event):
        if self.dataset.isMC:
            if self.cutflow == "SR":
                event.triggerWeight = ROOT.TotalTriggerSF(
                    event.firstLep.pdgId,
                    event.firstLep.pt,
                    event.firstLep.eta,
                    event.secondLep.pdgId,
                    event.secondLep.pt,
                    event.secondLep.eta,
                    event.htJet40[0],
                    )
            elif self.cutflow == "TightLoose":
                #event.triggerWeight = ROOT.TightLooseTriggerSF(
                event.triggerWeight = ROOT.TotalTriggerSF(
                    event.firstLep.pdgId,
                    event.firstLep.pt,
                    event.firstLep.eta,
                    event.secondLep.pdgId,
                    event.secondLep.pt,
                    event.secondLep.eta,
                    event.htJet40[0],
                    )
            event.weight *= event.triggerWeight
        return True
        
