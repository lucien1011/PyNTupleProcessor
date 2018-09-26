from Core.Module import Module
import ROOT

class Category(object):
    def __init__(self,lepCat,SRCat):
        self.lepCat = lepCat
        self.SRCat = SRCat

    def get_SRCat_str(self):
        return str(self.SRCat)

    def get_lepCat_str(self):
        return self.lepCat.Data()

class SRProducer(Module):
    def begin(self):
        ROOT.gSystem.Load("Library/Binning2016_cxx.so")

    def analyze(self,event):
        event.SRCategory = ROOT.signalRegionChargeSplit(
                int(event.nJetRA540[0]),
                int(event.nBJetMediumRA540[0]),
                event.met_pt[0],
                event.htJet40[0],
                event.mtmin,
                int(event.firstLep.pdgId),
                int(event.secondLep.pdgId),
                event.firstLep.pt,
                event.secondLep.pt,
                )
        event.leptonCategory = ROOT.leptonCategory(
                int(event.firstLep.pdgId),
                int(event.secondLep.pdgId),
                event.firstLep.pt,
                event.secondLep.pt,
                )

        event.cat = Category(event.leptonCategory,event.SRCategory)

        return True
