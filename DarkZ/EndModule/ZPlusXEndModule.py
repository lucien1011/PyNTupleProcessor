from Core.EndModule import EndModule

import os,ROOT,math,pickle

class SignMapMaker(EndModule):
    def __init__(self,outputPath,plots,sampleName="AllSample"):
        self.outputPath = outputPath
        self.plots = plots
        self.sampleName = sampleName

    def __call__(self,collector):
        self.makedirs_with_file_path(self.outputPath)
        
        outDict = {}
        for plot in self.plots:
            outDict[plot.key] = {}
            h = collector.getObj(self.sampleName,plot.rootSetting[1])
            for ibin in range(1,h.GetNbinsX()+1):
                lowBinEdge = h.GetXaxis().GetBinLowEdge(ibin)
                binContent = h.GetBinContent(ibin)
                outDict[plot.key][lowBinEdge] = binContent > 0.
        pickle.dump(outDict,open(self.outputPath,"w"))
