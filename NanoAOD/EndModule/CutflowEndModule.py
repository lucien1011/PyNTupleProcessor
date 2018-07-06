from Core.EndModule import EndModule

import os,ROOT,math
from collections import OrderedDict

from Utils.TableMaker import TableMaker

ROOT.gROOT.SetBatch(ROOT.kTRUE)

class CutflowEndModule(EndModule):
    def __init__(self,outputDir,plotFileName="CutflowEfficiency.tex",cutflows=[],histName="SumWeight",ignoreSumw=False):
        self.outputDir = outputDir
        self.plotFileName = plotFileName
        self.histName = histName
        self.cutflows = cutflows
        self.tableMaker = TableMaker()
        self.ignoreSumw = ignoreSumw

    def __call__(self,collector):
        self.makedirs(self.outputDir)
        tableDict = {}
        tableDict["nColumn"] = len(collector.mcSamples+collector.mergeSamples)+1
        tableDict["tab"] = "cutflow"
        tableDict["caption"] = "Cutflow Efficiency" 
        tableDict["tableList"] = []
        headerList = ["Cutflow",]
        for sample in collector.mcSamples+collector.mergeSamples:
            headerList.append(collector.sampleDict[sample].plotLabel)
        tableDict["tableList"].append(headerList)

        for cutflow in self.cutflows:
            cutflowList = [cutflow,]
            for sample in collector.mcSamples+collector.mergeSamples:
                if not self.ignoreSumw:
                    totalsum = collector.sampleDict[sample].sumw
                else:
                    h = collector.getObj(sample,self.histName+self.cutflows[0])
                totalsum = h.GetBinContent(1)
                h = collector.getObj(sample,self.histName+cutflow)
                genWeight = h.GetBinContent(1)
                cutflowList.append("%4.2f"%(genWeight/totalsum if totalsum else -1))
            tableDict["tableList"].append(cutflowList)
        self.tableMaker.makeTexFile(self.outputDir+self.plotFileName,tableDict,landscape=True)
