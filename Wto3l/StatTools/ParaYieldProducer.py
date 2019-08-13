from Core.Module import Module
import array

class ParaYieldProducer(Module):
    def __init__(self,name,systList=[],channelDict={},binning=[],postfix=""):
        self.name = name
        self.systList = systList
        #self.channelNames = ["4mu","4e","2e2mu","comb"]
        #self.channelNames = ["4mu","4e","2e2mu","2mu2e","comb"]
        self.channelNames = ["2mu","2e","comb"] if not channelDict else channelDict.keys()
        #if channelDict: self.channelNames.append("comb")
        self.channelDict = channelDict
        self.binning = [98000,4.,200.] if not binning else binning
        #self.binning = [110-1,array.array('d',[4.*1.02**i for i in range(110)]),]
        #self.norm_binning = [
        #        len(self.binning[1])-1,
        #        array.array('d',[(i-self.binning[1][0])/(self.binning[1][-1]-self.binning[1][0]) for i in self.binning[1]]),
        #        ]
        #self.hist_postfix = "-Norm" if not postfix else postfix

    def begin(self):
        for channelNames in self.channelNames:
            histName = channelNames
            histSettingList = [histName+"_mass1","TH1D",histName+"_mass1","",]+self.binning
            self.writer.book(*histSettingList)
            histSettingList = [histName+"_mass2","TH1D",histName+"_mass2","",]+self.binning
            self.writer.book(*histSettingList)
            '''
            for syst in self.systList:
                sysHistName = "_".join([channelName,syst.name])
                histSettingList = [sysHistName,"TH1D",sysHistName,"",]+self.binning
                self.writer.book(*histSettingList)
            '''   

    def analyze(self,event):
        #norm_value = (event.massZ2[0]-self.binning[-2])/(self.binning[-1]-self.binning[-2])
        eventWeight = event.weight

        #histName = "comb"
        #self.writer.objs[histName].Fill(event.mass1[0],eventWeight)

        for channelName,selFunc in self.channelDict.iteritems():
            if selFunc(event): 
                histName = channelName+"_mass1"
                self.writer.objs[histName].Fill(event.mass1,eventWeight)
                histName = channelName+"_mass2"
                self.writer.objs[histName].Fill(event.mass2,eventWeight)

        return True

    def end(self):
        for syst in self.systList:
            syst.factorFunc.end()

        for channelName,selFunc in self.channelDict.iteritems():
            selFunc.end()
