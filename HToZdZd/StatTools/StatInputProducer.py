from Core.Module import Module
import array

class StatInputProducer(Module):
    def __init__(self,name,systList=[],channelDict={}):
        self.name = name
        self.systList = systList
        self.channelNames = channelDict.keys()
        self.channelDict = channelDict

    def begin(self):
        for channelName,channel in self.channelDict.iteritems():
            channelHistSetting = [channel.histKey,]+channel.setting
            self.writer.book(*channelHistSetting)
            for syst in self.systList:
                nomHistName = self.writer[channel.histKey].GetName()
                sysHistName = "_".join([nomHistName,syst.name])
                sysHist = self.writer[channel.histKey].Clone(sysHistName)
                sysHistKey = channel.histKey+"_"+syst.name
                self.objs[sysHistKey] = sysHist
                self.rootObjs[sysHistKey] = sysHist

    def analyze(self,event):
        for channelName,channel in self.channelDict.iteritems():
            if channel.selFunc(event): 
                fillList = channel.fillFunc(event)
                self.writer.objs[channel.histKey].Fill(*fillList)
                for syst in self.systList:
                    sysHistKey = channel.histKey+"_"+syst.name
                    self.writer.objs[sysHistKey].Fill(*syst.fillFunc)
        return True

    def end(self):
        for syst in self.systList:
            syst.fillFunc.end()
        for channelName,channel in self.channelDict.iteritems():
            channel.selFunc.end()
            channel.fillFunc.end()
