from Core.EndModule import EndModule

import os,ROOT,math
from collections import OrderedDict

from Utils.TableMaker import TableMaker

ROOT.gROOT.SetBatch(ROOT.kTRUE)

class CutflowEndModule(EndModule):
    def __init__(self,outputDir,plotFileName="CutflowEfficiency.tex",cutflows=[],histName="SumWeight"):
        self.outputDir = outputDir
        self.plotFileName = plotFileName
        self.histName = histName
        self.cutflows = cutflows
        self.tableMaker = TableMaker()

    def __call__(self,collector):
        self.makedirs(self.outputDir)
        for sample in collector.mcSamples:
            totalsum = collector.sampleDict[sample].sumw
            tableDict = {}
            tableDict["nColumn"] = 2
            tableDict["tab"] = sample+"_cutflow"
            tableDict["caption"] = sample+" cutflow efficiency" 
            tableDict["tableList"] = []
            for cutflow in self.cutflows:
                h = collector.getObj(sample,self.histName+cutflow)
                genWeight = h.GetBinContent(1)
                tableDict["tableList"].append([cutflow,"%4.2f"%(genWeight/totalsum)])
            self.tableMaker.makeTexFile(self.outputDir+sample+"_"+self.plotFileName,tableDict)
