# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from Common.TreeProducer import TreeProducer

from RA5.Skimmer.BaselineSkimmer import BaselineSkimmer
from RA5.LeptonJetRecleaner.EventProducer import LeptonJetProducer 

from Config.BranchToAdd import branchesToAdd
from Config.BranchToKeep import branchesToKeep

from Core.Utils.LambdaFunc import LambdaFunc

import os,array

from DataMC.Heppy.Run2016.HaddMC import * 
from RA5.Dataset.Run2016.SyncMC import * 
from DataMC.Heppy.Run2016.SampleDefinition import *

from NanoAOD.Producer.GenWeightCounter import *

#out_path = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_LeptonJetRecleaner_TT_pow/"
out_path = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/SyncMC2016/TTW_RA5_sync_LeptonJetRecleaner/"
#out_path = "HeppyValidation/2018-07-16/"

nCores = 5
outputDir = out_path
nEvents = -1
disableProgressBar = False
justEndSequence = False
#componentList = [TT_pow]
componentList = [SyncMC]
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

leptonJetProducer       = LeptonJetProducer("LeptonJetProducer","Run2016")
treeProducer            = TreeProducer("TreeProducer",listOfBranchesToKeep=branchesToKeep,branchesToAdd=branchesToAdd)
baselineSkimmer         = BaselineSkimmer("SignalRegionSkimmer")
preskimCounter          = GenWeightCounter("GenWeightCounter",postfix="PreBaselineCut")
postskimCounter         = GenWeightCounter("GenWeightCounter",postfix="PostBaselineCut")

sequence = Sequence()
sequence.add(preskimCounter)
sequence.add(leptonJetProducer)
sequence.add(baselineSkimmer)
sequence.add(postskimCounter)
sequence.add(treeProducer)

endSequence = EndSequence(skipHadd=False)
endModuleOutputDir = out_path

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "SkimTree.root"
