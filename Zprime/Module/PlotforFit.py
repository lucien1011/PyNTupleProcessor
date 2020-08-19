import ROOT
from Core.Module import Module
import os,array,numpy
from Utils.DeltaR import deltaR

class PlotforFit(Module):

    def __init__(self,name):
        super(PlotforFit,self).__init__(name)
                        
    def begin(self):
        if "FitGaus_Z1" not in self.writer.objs:
            self.writer.book("FitGaus_Z1","TH1D","FitGaus_Z1","",480,0.,120.)
        if "FitGaus_Z2" not in self.writer.objs:
            self.writer.book("FitGaus_Z2","TH1D","FitGaus_Z2","",600,0.,100.)

    def analyze(self, event):
        if self.dataset.isData: return True
        #Fit Gaussian to each mass
        self.writer.objs["FitGaus_Z1"].Fill(event.massZ1[0],event.weight)
        self.writer.objs["FitGaus_Z2"].Fill(event.massZ2[0],event.weight)

        return True
