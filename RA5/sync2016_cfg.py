# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from RA5.Sequence.RecoSequence import sync_sequence
from RA5.Analyzer.Sync import LeptonSyncPrinter,JetSyncPrinter
from RA5.Config.MergeSampleDefinition import mergeSampleDict

from Core.Utils.LambdaFunc import LambdaFunc
from Core.Utils.WhichMachine import where

import os

#from DataMC.Heppy.Run2016.SampleDefinition import * 
#from RA5.Dataset.Run2016.SyncMC import SkimSyncMC
from RA5.Dataset.Run2016.SyncMC import SyncMC

from NanoAOD.Producer.GenWeightCounter import *

if where == "hpg":
    out_path = "/cms/data/store/user/t2/users/klo/HPG/RA5/Sync2016/2018-07-23/"
    outputDir = out_path
    endModuleOutputDir = out_path 
elif where == "ihepa":
    out_path = "Sync2016/2018-09-16/"
    outputDir = "/raid/raid7/lucien/SUSY/RA5/"+out_path
    endModuleOutputDir = "/home/lucien/public_html/SUSY/RA5/"+out_path
lepCats = ["HH","HL","LL"]

nCores = 1
nEvents = -1
disableProgressBar = True
justEndSequence = False
verbose = False
#componentList = [SkimSyncMC]
componentList = [SyncMC]
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

if not os.path.exists(endModuleOutputDir):
    os.makedirs(endModuleOutputDir)

sequence = sync_sequence 
lepSyncPrinter = LeptonSyncPrinter("SyncPrinter",endModuleOutputDir+"uf_TTW_80X_dump_leptons.txt")
jetSyncPrinter = JetSyncPrinter("SyncPrinter",endModuleOutputDir+"uf_TTW_80X_dump_jets.txt")
sequence.add(lepSyncPrinter)
sequence.add(jetSyncPrinter)

endSequence = EndSequence(haddAllSamples=True)

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "SyncFile.root"
