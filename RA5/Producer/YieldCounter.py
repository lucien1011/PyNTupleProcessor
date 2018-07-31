import ROOT
from Core.Module import Module

class YieldCounter(Module):
    def __init__(self,name,postfix=""):
        super(YieldCounter,self).__init__(name)
        self.postfix = postfix

    def analyze(self,event):
        if event.cat.jetCat != "0":
            if "YieldCount"+event.cat.lepCat+event.cat.jetCat not in self.writer.objs:
                self.writer.book("YieldCount"+event.cat.lepCat+event.cat.jetCat,"TH1D","YieldCount"+event.cat.lepCat+event.cat.jetCat,"",1,-0.5,0.5)
        if event.cat.jetCat != "0":
            self.writer.objs["YieldCount"+event.cat.lepCat+event.cat.jetCat].Fill(0.)
        return True
