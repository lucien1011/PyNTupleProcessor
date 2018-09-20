import ROOT
from Core.Module import Module

class YieldCounter(Module):
    def __init__(self,name,postfix=""):
        super(YieldCounter,self).__init__(name)
        self.postfix = postfix

    def analyze(self,event):
        if event.cat.SRCat != "0":
            if "YieldCount"+event.cat.lepCat+event.cat.SRCat not in self.writer.objs:
                self.writer.book("YieldCount"+event.cat.lepCat+event.cat.SRCat,"TH1D","YieldCount"+event.cat.lepCat+event.cat.SRCat,"",1,-0.5,0.5)
        if event.cat.SRCat != "0":
            self.writer.objs["YieldCount"+event.cat.lepCat+event.cat.SRCat].Fill(0.,event.weight)
        return True
