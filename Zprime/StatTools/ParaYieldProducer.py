from Core.Module import Module

mZ1_var_name = "mZ1"
mZ2_var_name = "mZ2"

class ParaYieldProducer(Module):
    def __init__(self,name,channelDict={},binning=[],norm_binning=[],postfix=""):
        self.name = name
        self.channelNames = channelDict.keys()
        if channelDict: self.channelNames.append("comb")
        self.channelDict = channelDict
        self.mZ1_binning = [12000,0.,120.] if not binning else binning
        self.mZ2_binning = [12000,0.,120.] if not binning else binning
        self.hist_postfix = "-Norm" if not postfix else postfix

    def begin(self):
        for channelName in self.channelNames:
            histName = mZ1_var_name+'_'+channelName 
            histSettingList = [histName,"TH1D",histName,"",]+self.mZ1_binning
            self.writer.book(*histSettingList)
            histName = mZ2_var_name+'_'+channelName 
            histSettingList = [histName,"TH1D",histName,"",]+self.mZ2_binning
            self.writer.book(*histSettingList)

    def analyze(self,event):
        histName = "comb"
        self.writer.objs[mZ1_var_name+"_"+histName].Fill(event.massZ1[0],event.weight)
        self.writer.objs[mZ2_var_name+"_"+histName].Fill(event.massZ2[0],event.weight)
        for channelName,selFunc in self.channelDict.iteritems():
            if selFunc(event): 
                histName = channelName
                self.writer.objs[mZ1_var_name+"_"+histName].Fill(event.massZ1[0],event.weight)
                self.writer.objs[mZ2_var_name+"_"+histName].Fill(event.massZ2[0],event.weight)
        return True

    def end(self):
        for channelName,selFunc in self.channelDict.iteritems():
            selFunc.end()
