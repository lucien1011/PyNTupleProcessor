import ROOT,os,copy

from Core.Collector import Collector

from DarkZ.plot_Run2016_DarkPhoton_m4lSB_ClosureTest_cfg import componentList,outputInfo,mergeSampleDict

import math,argparse

# ____________________________________________________________________________________________________________________________________________ ||
variables       = [
                    "Z2_mass",
                    ]
dataSample      = "Data2016"
mcSamples       = [
                    "ggZZ",
                    "qqZZTo4L",
                    ]
rebin           = 3

# ____________________________________________________________________________________________________________________________________________ ||
parser = argparse.ArgumentParser()
parser.add_argument("--inputDir",action="store")
parser.add_argument("--outputDir",action="store")
parser.add_argument("--verbose",action="store_true")

option = parser.parse_args()

# ____________________________________________________________________________________________________________________________________________ ||
outputInfo.outputDir    = option.inputDir
outputInfo.TFileName    = "ClosureTest.root"

# ____________________________________________________________________________________________________________________________________________ ||
collector = Collector()
collector.makeSampleList(componentList)
collector.makeMergedSampleList(componentList,mergeSampleDict)
collector.openFiles(collector.samples+collector.mergeSamples,outputInfo)

# ____________________________________________________________________________________________________________________________________________ ||
if not os.path.exists(os.path.abspath(option.outputDir)):
    os.makedirs(os.path.abspath(option.outputDir))
c = ROOT.TCanvas()
for var in variables:
    if option.verbose: print "*"*100
    dataHist = collector.getObj(dataSample,var)
    if option.verbose: print "Data: ",dataHist.Integral()
    outHist = dataHist.Clone(var+"_shape")
    outHist.Rebin(rebin)
    for ibin in range(1,outHist.GetNbinsX()+1):
        if outHist.GetBinContent(ibin):
            outHist.SetBinError(ibin,outHist.GetBinContent(ibin))
        else:
            outHist.SetBinError(ibin,0.)
    for mcSample in mcSamples:
        tempHist = collector.getObj(mcSample,var)
        tempHist.Rebin(rebin)
        outHist.Add(tempHist,-1)
        if option.verbose: print mcSample+": ",tempHist.Integral()
    outHist.SetStats(0)
    outHist.Draw()
    c.SaveAs(os.path.join(option.outputDir,var+".pdf"))
