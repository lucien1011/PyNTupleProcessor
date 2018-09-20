import ROOT
from Core.Module import Module
import os,array

class Btageff(Module):

    def __init__(self,name):
        super(Btageff,self).__init__(name)
    
    def begin(self):
        #pt_bins = [0.,20.,40.,200.]
        #array_pt_bins = array('d',pt_bins)
        #self.writer.book("BTageffNum","TH2D","BTageffNum",3,array_pt_bins,10,-2.4,2.4)
        #self.writer.book("BTageffDem","TH2D","BTageffDem",3,array_pt_bins,10,-2.4,2.4)
        #self.writer.book("CTageffNum","TH2D","CTageffNum",3,array_pt_bins,10,-2.4,2.4)
        #self.writer.book("CTageffDem","TH2D","CTageffDem",3,array_pt_bins,10,-2.4,2.4)
        #self.writer.book("LTageffNum","TH2D","LTageffNum",3,array_pt_bins,10,-2.4,2.4)
        #self.writer.book("LTageffDem","TH2D","LTageffDem",3,array_pt_bins,10,-2.4,2.4)
        #self.writer.book("BTageffNum","TH2D","BTageffNum",10,0.,200.,10,-2.4,2.4)
        #self.writer.book("BTageffDem","TH2D","BTageffDem",10,0.,200.,10,-2.4,2.4)
        #self.writer.book("CTageffNum","TH2D","CTageffNum",10,0.,200.,10,-2.4,2.4)
        #self.writer.book("CTageffDem","TH2D","CTageffDem",10,0.,200.,10,-2.4,2.4)
        #self.writer.book("LTageffNum","TH2D","LTageffNum",10,0.,200.,10,-2.4,2.4)
        #self.writer.book("LTageffDem","TH2D","LTageffDem",10,0.,200.,10,-2.4,2.4)
        if "BTageffNum" not in self.writer.objs:
            self.writer.book("BTageffNum","TH2D","BTageffNum","",10,0.,200.,10,-2.4,2.4)
        if "BTageffDem" not in self.writer.objs:
            self.writer.book("BTageffDem","TH2D","BTageffDem","",10,0.,200.,10,-2.4,2.4)
        if "CTageffNum" not in self.writer.objs:
            self.writer.book("CTageffNum","TH2D","CTageffNum","",10,0.,200.,10,-2.4,2.4)
        if "CTageffDem" not in self.writer.objs:
            self.writer.book("CTageffDem","TH2D","CTageffDem","",10,0.,200.,10,-2.4,2.4)
        if "LTageffNum" not in self.writer.objs:
            self.writer.book("LTageffNum","TH2D","LTageffNum","",10,0.,200.,10,-2.4,2.4)
        if "LTageffDem" not in self.writer.objs:
            self.writer.book("LTageffDem","TH2D","LTageffDem","",10,0.,200.,10,-2.4,2.4)



    def analyze(self, event):
        if self.dataset.isData: return True
        for jet in event.jets25:
            if abs(jet.hadronFlavour) == 5:
                self.writer.objs["BTageffDem"].Fill(jet.pt,jet.eta,event.weight)
                if jet.btagCSVV2 > 0.8484:
                    self.writer.objs["BTageffNum"].Fill(jet.pt,jet.eta,event.weight)

            if abs(jet.hadronFlavour) == 4:
                self.writer.objs["CTageffDem"].Fill(jet.pt,jet.eta,event.weight)
                if jet.btagCSVV2 > 0.8484:
                    self.writer.objs["CTageffNum"].Fill(jet.pt,jet.eta,event.weight)

            if abs(jet.hadronFlavour) == 0:
                self.writer.objs["LTageffDem"].Fill(jet.pt,jet.eta,event.weight)
                if jet.btagCSVV2 > 0.8484:
                    self.writer.objs["LTageffNum"].Fill(jet.pt,jet.eta,event.weight)

        return True



