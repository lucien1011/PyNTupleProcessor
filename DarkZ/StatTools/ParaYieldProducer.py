from Core.Module import Module

class ParaYieldProducer(Module):
    def __init__(self,name,systList=[]):
        self.name = name
        self.systList = systList
        #self.channelNames = ["4mu","4e","2e2mu","comb"]
        self.channelNames = ["4mu","4e","2e2mu","2mu2e","comb"]
        self.binning = [1200,0.,120.]

    def begin(self):
        for channelName in self.channelNames:
            histName = channelName 
            histSettingList = [histName,"TH1D",histName,"",]+self.binning
            self.writer.book(*histSettingList)
            for syst in self.systList:
                sysHistName = "_".join([channelName,syst.name])
                histSettingList = [sysHistName,"TH1D",sysHistName,"",]+self.binning
                self.writer.book(*histSettingList)


    def analyze(self,event):
        histName = "comb"
        self.writer.objs[histName].Fill(event.massZ2[0],event.weight)
         
        if event.mass4mu[0] > 0. and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13:
            channelName = "4mu"
        elif event.mass4e[0] > 0. and abs(event.idL3[0]) == 11 and abs(event.idL4[0]) == 11:
            channelName = "4e"
        elif event.mass2e2mu[0] > 0. and abs(event.idL3[0]) == 11 and abs(event.idL4[0]) == 11:
            channelName = "2mu2e"
        elif event.mass2e2mu[0] > 0. and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13:
            channelName = "2e2mu"

        histName = channelName
        self.writer.objs[histName].Fill(event.massZ2[0],event.weight)

        for syst in self.systList:
            sysHistName = "_".join(["comb",syst.name])
            self.writer.objs[sysHistName].Fill(event.massZ2[0],event.weight*syst.factorFunc(event))

            sysHistName = "_".join([channelName,syst.name])
            self.writer.objs[sysHistName].Fill(event.massZ2[0],event.weight*syst.factorFunc(event))
        return True

    def end(self):
        for syst in self.systList:
            syst.factorFunc.end() 
