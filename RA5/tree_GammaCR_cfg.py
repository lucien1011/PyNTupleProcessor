# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from Common.TreeProducer import TreeProducer

from RA5.Sequence.RecoSequence import gamma_cr_skim_sequence

from Config.BranchToAdd import branchesToAdd
from Config.BranchToKeep import branchesToKeep

from Core.Utils.LambdaFunc import LambdaFunc

import os,array

from RA5.Dataset.Run2016.Sept18_v1 import *
from RA5.Dataset.Run2016.Sept18_v1_Data import *

from NanoAOD.Producer.GenWeightCounter import *

out_path  = "/raid/raid7/lucien/SUSY/RA5/HeppyTree/Sept18_v1_GammaCRSkim/"

nCores                      = 5
outputDir                   = out_path
nEvents                     = -1
disableProgressBar          = False
justEndSequence             = False
componentList               = [c for c in dataComponentDict.values() if "2016H" not in c.name] + componentDict.values() 
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

treeProducer            = TreeProducer("TreeProducer")#,listOfBranchesToKeep=branchesToKeep,branchesToAdd=branchesToAdd)

sequence = gamma_cr_skim_sequence
sequence.add(treeProducer)

endSequence = EndSequence(skipHadd=False)
endModuleOutputDir = out_path

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "SkimTree.root"
