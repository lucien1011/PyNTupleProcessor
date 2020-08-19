import os,copy,ROOT

from RA5.StatFW.DataCard import *
from RA5.StatFW.SR import *
from RA5.StatFW.Systematic import *
from RA5.StatFW.Process import *
from RA5.StatFW.Reader import *
from RA5.StatFW.Channel import Bin

from Core.Collector import Collector

from RA5.stat_input_TTWW_cfg import componentList,mergeSampleDict,outputInfo

import math,argparse
# ____________________________________________________________________________________________________________________________________________ ||
parser = argparse.ArgumentParser()
parser.add_argument("--inputDir",action="store")
parser.add_argument("--outputDir",action="store")
parser.add_argument("--makeTextFile",action="store_true")
parser.add_argument("--verbose",action="store_true")
parser.add_argument("--baseline",action="store_true")
parser.add_argument("--sigModel",action="store")

option = parser.parse_args()

# ____________________________________________________________________________________________________________________________________________ ||
lnSystFilePath      = "/home/lucien/UF-PyNTupleRunner/RA5/StatFW/Config/CommonSyst.txt"
allSampleDir        = "AllSample"
fileName            = "StatInput.root"
setDataToMC         = True
addMCStat           = True
sigModel            = "TTWW" if not option.sigModel else option.sigModel
fixWidthStr         = "%15s"
fixWidthFloat       = "%15.2f"
if option.inputDir: outputInfo.outputDir = option.inputDir

# ____________________________________________________________________________________________________________________________________________ ||
collector = Collector()
collector.makeSampleList(componentList)
collector.makeMergedSampleList(componentList,mergeSampleDict)
collector.openFiles(collector.samples+collector.mergeSamples,outputInfo)

# ____________________________________________________________________________________________________________________________________________ ||
# syst
lnSystReader = LogNormalSystReader()
commonLnSystematics = lnSystReader.makeLnSyst(lnSystFilePath)

if not os.path.exists(os.path.abspath(option.outputDir)):
    os.makedirs(os.path.abspath(option.outputDir))

binDict = {}
inputFileAll = ROOT.TFile(os.path.join(option.inputDir,allSampleDir,fileName))
for k in inputFileAll.GetListOfKeys():
    objName = k.GetName()
    if "DiscardedEvent" in objName: continue
    lepCat = objName.split("_")[1]
    SRCat = objName.split("_")[2]
    keyForDict = lepCat+"_SR"+SRCat
    binDict[keyForDict] = SR(int(SRCat),lepCat)
    binDict[keyForDict].binList = []
    binDict[keyForDict].binList.append(
        Bin("SR",sysFile=lnSystFilePath,inputBinName="SR"),
        )

SRList = binDict.keys()
SRList.sort()
for key in SRList:
    eachSR = binDict[key]
    for bin in eachSR.binList:
        totalBkgCount = 0.
        for bkgName in collector.mergeSamples: 
            histName = "Central_"+key.replace("SR","")
            try:
                hist = collector.getObj(bkgName,histName)
                count = hist.GetBinContent(1)
                error = hist.GetBinError(1)
            except AttributeError:
                count = 0.
                error = 0.
            process = Process(bkgName,count if count >= 0. else 0.,error)
            totalBkgCount += count if count >= 0. else 0.
            bin.processList.append(process)
            if count > 0.:
                process.mcStatUnc = lnNSystematic("_".join([eachSR.getBinName(),bkgName,"MCStatUnc",]),[bkgName,],1.+error/count)
            else:
                process.mcStatUnc = None
            if option.makeTextFile:
                rowStr += fixWidthFloat%count+" "
        
        sigCount = 0.
        for sample in collector.signalSamples: 
            #histName = "_".join([window.makeHistName(),sample,bin.name,])
            histName = "Central_"+key.replace("SR","")
            hist = collector.getObj(sample,histName)
            try:
                hist = collector.getObj(sample,histName)
                count = hist.GetBinContent(1)
                error = hist.GetBinError(1)
            except AttributeError:
                count = 0.
                error = 0.
            sigCount += count
        print key, ",", sigCount       
