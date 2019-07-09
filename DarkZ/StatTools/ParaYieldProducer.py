from Core.Module import Module
import array

class ParaYieldProducer(Module):
    def __init__(self,name,systList=[],channelDict={},binning=[],norm_binning=[],postfix=""):
        self.name = name
        self.systList = systList
        #self.channelNames = ["4mu","4e","2e2mu","comb"]
        #self.channelNames = ["4mu","4e","2e2mu","2mu2e","comb"]
        self.channelNames = ["2mu","2e","comb"] if not channelDict else channelDict.keys()
        if channelDict: self.channelNames.append("comb")
        self.channelDict = channelDict
        self.binning = [12000,4.,35.] if not binning else binning
        self.norm_binning = [6000,0.,1.] if not norm_binning else norm_binning
        #self.binning = [110-1,array.array('d',[4.*1.02**i for i in range(110)]),]
        #self.norm_binning = [
        #        len(self.binning[1])-1,
        #        array.array('d',[(i-self.binning[1][0])/(self.binning[1][-1]-self.binning[1][0]) for i in self.binning[1]]),
        #        ]
        self.hist_postfix = "-Norm" if not postfix else postfix

    def begin(self):
        for channelName in self.channelNames:
            histName = channelName 
            histSettingList = [histName,"TH1D",histName,"",]+self.binning
            self.writer.book(*histSettingList)
            histSettingList = [histName+self.hist_postfix,"TH1D",histName+self.hist_postfix,"",]+self.norm_binning
            self.writer.book(*histSettingList)
            for syst in self.systList:
                sysHistName = "_".join([channelName,syst.name])
                histSettingList = [sysHistName,"TH1D",sysHistName,"",]+self.binning
                self.writer.book(*histSettingList)
                histSettingList = [sysHistName+self.hist_postfix,"TH1D",sysHistName+self.hist_postfix,"",]+self.norm_binning
                self.writer.book(*histSettingList)

    def analyze(self,event):
        #norm_value = (event.massZ2[0]-self.binning[1][0])/(self.binning[1][-1]-self.binning[1][0])
        norm_value = (event.massZ2[0]-self.binning[-2])/(self.binning[-1]-self.binning[-2])

        histName = "comb"
        self.writer.objs[histName].Fill(event.massZ2[0],event.weight)
        self.writer.objs[histName+self.hist_postfix].Fill(norm_value,event.weight)

        for channelName,selFunc in self.channelDict.iteritems():
            if selFunc(event): 
                histName = channelName
                self.writer.objs[histName].Fill(event.massZ2[0],event.weight)
                self.writer.objs[histName+self.hist_postfix].Fill(norm_value,event.weight)

        return True

    def end(self):
        for syst in self.systList:
            syst.factorFunc.end()

        for channelName,selFunc in self.channelDict.iteritems():
            selFunc.end()
