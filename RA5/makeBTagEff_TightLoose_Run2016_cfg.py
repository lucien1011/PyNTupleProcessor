# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Config.MergeSampleDefinition import mergeSampleDict
#from RA5.Skimmer.SignalRegionSkimmer import SignalRegionSkimmer

from RA5.Sequence.RecoSequence import tl_rpv_sequence

from Common.BTagEffAnalyzer import BTagEffAnalyzer
from Common.BTagEffEndModule import BTagEffEndModule

from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.WhichMachine import where

import os

from RA5.Dataset.Run2016.Sept18_v1_TightLoose import skimComponentDict

if where == "hpg":
    out_path = "/cms/data/store/user/t2/users/klo/HPG/RA5/RPV/DataMCDistributions/2018-09-12_HLTEmulation/"
    outputDir = out_path
    endModuleOutputDir = out_path 
elif where == "ihepa":
    out_path = "TightLoose/BTagEfficiency/2018-10-16/"
    outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
    endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path
lepCats = [""]

nCores                      = 5
nEvents                     = -1
disableProgressBar          = False
justEndSequence             = False
verbose                     = False
componentList               = [ c for c in skimComponentDict.values() if c.isMC]
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

btagEffAna      = BTagEffAnalyzer("BTagEffAnalyzer")
btagEffEnd      = BTagEffEndModule(endModuleOutputDir,cutflow="TightLoose",)

sequence = tl_rpv_sequence
sequence.add(btagEffAna)

endSequence = EndSequence(skipHadd=False,haddAllSamples=True)
endSequence.add(btagEffEnd)

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "BTagEfficiency.root"
