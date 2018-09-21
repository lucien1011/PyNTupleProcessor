from Core.Module import Module
import ROOT

class SRProducer(Module):
    def begin(self):
        ROOT.gSystem.Load("Library/Binning2016_cxx.so")

    def analyze(self,event):
        event.SRCategory = ROOT.signalRegionChargeSplit(
                event.nJetRA540[0],
                event.nBJetMediumRA540[0],
                event.met_pt[0],
                event.mtmin,
                event.firstLep.pdgId,
                event.secondLep.pdgId,
                event.firstLep.pt,
                event.secondLep.pt,
                )
        event.leptonCategory = ROOT.leptonCategory(
                event.firstLep.pdgId,
                event.secondLep.pdgId,
                event.firstLep.pt,
                event.secondLep.pt,
                )

        event.cat = Category()
        event.cat.lepCat = event.leptonCategory
        event.cat.SRCat = event.SRCategory 

        return True
