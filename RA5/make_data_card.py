import os,copy,ROOT

from RA5.StatFW.DataCard import *
from RA5.StatFW.SR import *
from RA5.StatFW.Systematic import *
from RA5.StatFW.Process import *
from RA5.StatFW.Reader import *
from RA5.StatFW.Channel import Bin

from Core.Collector import Collector

from RA5.stat_input_cfg import componentList,mergeSampleDict,outputInfo

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
sigModel            = "SMS-T1qqqqL_1500" if not option.sigModel else option.sigModel
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
    if lepCat != "HH": continue
    if option.baseline and lepCat == "HH" and int(SRCat) > 52: continue
    if "-1" in SRCat: continue
    keyForDict = lepCat+"_SR"+SRCat
    binDict[keyForDict] = SR(int(SRCat),lepCat)
    binDict[keyForDict].binList = []
    binDict[keyForDict].binList.append(
            Bin("SR",sysFile=lnSystFilePath,inputBinName="SR"),
            )
if option.makeTextFile:
    textFile = open(option.outputDir+"/Yield.txt","w")
    headerStr = fixWidthStr%"SR"+" "
    for bkgName in collector.mergeSamples:
        headerStr += fixWidthStr%bkgName+" "
    headerStr += fixWidthStr%"Data"+" "
    for sigSample in collector.signalSamples:
        headerStr += fixWidthStr%sigSample+" "
    textFile.write(headerStr+"\n")

combTextFile = open(option.outputDir+"/DataCardList.txt","w")
SRList = binDict.keys()
SRList.sort()
for key in SRList:
    eachSR = binDict[key]
    if option.verbose: print "*"*100
    if option.verbose: print eachSR.getBinName()
    if option.makeTextFile:
        rowStr = fixWidthStr%key+" "
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

        if option.verbose: print "Total bkg count: ", totalBkgCount
        
        dataCount = 0.
        for sample in collector.dataSamples:
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
            dataCount += count
        if option.makeTextFile:
            rowStr += fixWidthFloat%dataCount+" "
        bin.data = Process("data_obs",int(dataCount) if not setDataToMC else int(totalBkgCount),math.sqrt(int(dataCount)))
        if option.verbose: print "Total data count: ", dataCount
        
        for sigSample in collector.signalSamples:
            try:
                hist = collector.getObj(sigSample,histName)
                count = hist.GetBinContent(1)
                error = hist.GetBinError(1)
            except AttributeError:
                count = 0.
                error = 0.
            if bin.isSignal(sigSample) and sigModel in sigSample:
                if option.makeTextFile:
                    rowStr += fixWidthFloat%count+" "
                break
            else:
                if option.makeTextFile:
                    rowStr += fixWidthFloat%(-1)+" "

        #histName = "_".join([window.makeHistName(),sigSample,bin.name,])
        histName = "Central_"+key.replace("SR","")
        sigHist = collector.getObj(sigSample,histName)
        try:
            hist = collector.getObj(sigSample,histName)
            count = hist.GetBinContent(1)
            error = hist.GetBinError(1)
        except AttributeError:
            count = 0.
            error = 0.
        if option.verbose: print "Total signal count: ", count
        sigProcess = Process(sigSample,count,error)
        bin.processList.append(sigProcess)
        if count > 0.:
                sigProcess.mcStatUnc = lnNSystematic("_".join([eachSR.getBinName(),sigSample,"MCStatUnc",]),[sigSample,],1.+error/count,)
        else:
            sigProcess.mcStatUnc = None
        bin.systList = []
        for syst in commonLnSystematics:
            bin.systList.append(copy.deepcopy(syst))
        for process in bin.processList:
            if addMCStat and process.mcStatUnc:
                bin.systList.append(process.mcStatUnc)
    if option.makeTextFile:
        textFile.write(rowStr+"\n")

    dataCard = DataCard(eachSR)
    dataCard.makeCard(option.outputDir,eachSR.binList) 
    combTextFile.write(dataCard.getBinName()+" "+dataCard.makeOutFileName(".txt","")+"\n")
combTextFile.close()
