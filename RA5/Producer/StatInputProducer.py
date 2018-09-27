import ROOT
from Core.Module import Module

class StatInputProducer(Module):
    def __init__(self,name,systList):
        super(StatInputProducer,self).__init__(name)
        self.systList = systList
        self.varyList = ["Up","Down"]
        self.systEvtAttrs = []
        for vary in self.varyList:
            for systName in self.systList:
                self.systEvtAttrs.append(systName+vary)
        self.nominalHistName = "Central"

    def analyze(self,event):
        # Fill nominal
        nominalKey = "_".join([self.nominalHistName,event.cat.get_lepCat_str(),event.cat.get_SRCat_str(),])
        if nominalKey not in self.writer.objs:
            self.writer.book(nominalKey,"TH1D",nominalKey,"",1,-0.5,0.5)
        self.writer.objs[nominalKey].Fill(0.,event.weight)

        # Fill syst variation
        for systName in self.systEvtAttrs:
            systKey = "_".join([systName,event.cat.get_lepCat_str(),event.cat.get_SRCat_str(),])
            if systKey not in self.writer.objs:
                self.writer.book(systKey,"TH1D",systKey,"",1,-0.5,0.5)
            self.writer.objs[systKey].Fill(0.,getattr(event,systName))
        return True
