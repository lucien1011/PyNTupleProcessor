from Core.Module import Module
import ROOT

class HLTWeighter(Module):
    def begin(self):
        ROOT.gSystem.Load("Library/TriggerSF_Moriond2017_cxx.so")
        
    def analyze(self,event):
        if self.dataset.isMC:
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
        
