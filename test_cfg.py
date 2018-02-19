# UF Heppy Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 

from RPV.Module.EventPrinter import EventPrinter

nCores = 2
inputDir = "/afs/cern.ch/work/k/klo/SUSY/RPV/TreeProduction/CMSSW_8_0_25/src/CMGTools/RPV/cfg/TEST_01/"
outputDir = "/afs/cern.ch/work/k/klo/SUSY/RPV/UF-PyNTupleRunner/Log/20180219/test01/"
componentList = ["SMS_RPV_madgraphMLM_1","SMS_RPV_madgraphMLM",]
nEvents = -1
disableProgressBar = False
eventPrinter = EventPrinter("EventPrinter")
sequence = Sequence()
sequence.add(eventPrinter)

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "test1.root"
