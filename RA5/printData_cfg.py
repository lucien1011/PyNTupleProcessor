# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Config.MergeSampleDefinition import mergeSampleDict

from RA5.Sequence.RecoSequence import low_met_sequence
from RA5.Analyzer.EventPrinter import EventPrinter

from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.WhichMachine import where

import os

from RA5.Dataset.Run2016.Sept18_v1_Data import *
#from RA5.Dataset.Run2016.Sept18_v1_skim import *

out_path = "RPV/EventList/rpv_binning2016_v6_136p3fb-1/2019-01-17/"
outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path

nCores = 5
nEvents = -1
disableProgressBar = False
justEndSequence = False
verbose = False
#componentList = [ c for c in skimComponentDict.values() if c.isData ]
componentList = dataComponentDict.values()
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 136.3
    for component in dataset.componentList:
        component.maxEvents = nEvents

eventPrinter = EventPrinter("EventPrinter",endModuleOutputDir)
sequence = low_met_sequence 
sequence.add(eventPrinter)

endSequence = EndSequence(skipHadd=False,haddAllSamples=True)

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "dummy.root"
