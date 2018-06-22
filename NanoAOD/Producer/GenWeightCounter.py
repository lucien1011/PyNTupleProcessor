import ROOT

from Core.Module import Module

class GenWeightCounter(Module):
    def begin(self):
        self.writer.book("SumWeight","TH1D","SumWeight","",1,-0.5,0.5)
        self.writer.book("EventCount","TH1D","EventCount","",1,-0.5,0.5)
        
    def analyze(self,event):
        self.writer.objs["SumWeight"].Fill(0.,event.genWeight[0])
        self.writer.objs["EventCount"].Fill(0.)
        return True
