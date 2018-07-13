
from Core.EndModule import EndModule

import os,ROOT,math
from collections import OrderedDict

ROOT.gROOT.SetBatch(ROOT.kTRUE)

markerStyle = 2
markerSize = 3

class EfficiencyEndModule(EndModule):
    def __init__(self,outputDir,plotFileName="SignalEfficiency.pdf"):
        self.outputDir = outputDir
        self.plotFileName = plotFileName
        self.histName_SelSumWeight = "SumWeight"

    def __call__(self,collector):
        effMap = self.makeEfficiencyMap(collector)
        if effMap:
            self.makedirs(self.outputDir)
            c = ROOT.TCanvas()
            effHist = ROOT.TH1D("EffMap","",len(effMap),-0.5,len(effMap)-0.5)
            ibin = 1
            for sample,eff in effMap.iteritems():
                effHist.SetBinContent(ibin,eff)
                effHist.GetXaxis().SetBinLabel(ibin,sample)
                ibin += 1
            effHist.SetStats(0)
            effHist.SetMarkerStyle(markerStyle)
            effHist.SetMarkerSize(markerSize)
            effHist.GetYaxis().SetRangeUser(0.,1.)
            effHist.Draw("p")
            c.SaveAs(self.outputDir+self.plotFileName)


    def makeEfficiencyMap(self,collector):
        effMap = OrderedDict()
        for sample in collector.mcSamples:
            h = collector.getObj(sample,self.histName_SelSumWeight)
            effMap[sample] = h.GetBinContent(1)/collector.sampleDict[sample].sumw
        return effMap

    @staticmethod
    def makedirs(outputDir):
        if not os.path.exists(os.path.abspath(outputDir)):
            os.makedirs(os.path.abspath(outputDir))
