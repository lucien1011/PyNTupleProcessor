import os,copy

from DarkZ.StatTools.DataCard import *
from DarkZ.StatTools.MassWindow import *
from DarkZ.StatTools.Systematic import *
from DarkZ.StatTools.Process import *
from DarkZ.StatTools.Reader import *

from Core.Collector import Collector

from DarkZ.stat_input_cfg import componentList,outputInfo

import math

inputDir = "/raid/raid7/lucien/Higgs/DarkZ/StatInput/SignalSelection_v1/2018-07-26/"
lnSystFilePath = "/home/lucien/UF-PyNTupleRunner/DarkZ/StatTools/Syst.txt"
outputDir = "./StatTest/"
mass_window_list = [
        MassWindow(15,0.02),
        MassWindow(20,0.02),
        MassWindow(25,0.02),
        MassWindow(30,0.02),
        ]

lnSystReader = LogNormalSystReader()
lnSystematics = lnSystReader.makeLnSyst(lnSystFilePath)

collector = Collector()
collector.makeSampleList(componentList)
collector.openFiles(collector.samples,outputInfo)

if not os.path.exists(os.path.abspath(outputDir)):
    os.makedirs(os.path.abspath(outputDir))

for window in mass_window_list:
    window.processList = []
    dataCount = 0.
    for bkgName in collector.bkgSamples:
        hist = collector.getObj(bkgName,window.makeHistName())
        count = hist.GetBinContent(1)
        dataCount += count
        error = hist.GetBinError(1)
        process = Process(bkgName,count,error)
        window.processList.append(process)
    window.data = Process("data_obs",int(dataCount),math.sqrt(int(dataCount)))
    for sigSample in collector.signalSamples:
        if window.matchSample(sigSample): break
    sigHist = collector.getObj(sigSample,window.makeHistName())
    window.processList.append(Process(sigSample,sigHist.GetBinContent(1),sigHist.GetBinError(1)))
    window.systList = []
    for syst in lnSystematics:
        window.systList.append(copy.deepcopy(syst))
    dataCard = DataCard(window) 
    dataCard.makeCard(outputDir,)

collector.closeFiles()
