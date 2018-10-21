# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from Common.TreeProducer import TreeProducer

from RA5.Sequence.RecoSequence import rpv_skim_sequence

from Core.Utils.LambdaFunc import LambdaFunc

import os,array

from RA5.Dataset.Run2016.Sept18_v1 import *
from RA5.Dataset.Run2016.Sept18_v1_Data import *

from NanoAOD.Producer.GenWeightCounter import *

out_path = "/raid/raid7/lucien/SUSY/RA5/HeppyTree/Sept18_v1_skim_v1.0_Include3LepInLowMETBin_181019/"

nCores                      = 6
outputDir                   = out_path
nEvents                     = -1
disableProgressBar          = False
justEndSequence             = False
componentList               = componentDict.values() + dataComponentDict.values()

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

treeProducer                = TreeProducer("TreeProducer")

sequence                    = rpv_skim_sequence
sequence.add(treeProducer)

endSequence                 = EndSequence(skipHadd=False)
endModuleOutputDir          = out_path

outputInfo                  = OutputInfo("OutputInfo")
outputInfo.outputDir        = outputDir
outputInfo.TFileName        = "SkimTree.root"
