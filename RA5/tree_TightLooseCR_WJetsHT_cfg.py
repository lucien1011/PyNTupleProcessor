# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from Common.TreeProducer import TreeProducer

from RA5.Sequence.RecoSequence import tl_rpv_skim_sequence

from Config.BranchToAdd import branchesToAdd
from Config.BranchToKeep import branchesToKeep

from Core.Utils.LambdaFunc import LambdaFunc

import os,array

from RA5.Dataset.Run2016.Sept18_v1 import *
from RA5.Dataset.Run2016.Sept18_v1_Data import *
#from RA5.Dataset.Run2016.Sept18_v1_skim import *
from RA5.Dataset.Run2016.Sept18_v1_SMS import sigComponentDict

from NanoAOD.Producer.GenWeightCounter import *

#out_path = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v2_LeptonJetRecleaner/"
#out_path = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v2_LeptonJetRecleaner_rpv/"
#out_path = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/SyncMC2016/TTW_RA5_sync_LeptonJetRecleaner/"
#out_path = "/raid/raid7/lucien/SUSY/RA5/HeppyTree/SkimMC2016/July18_v2_LeptonJetRecleaner_rpv/"
out_path  = "/raid/raid7/lucien/SUSY/RA5/HeppyTree/Sept18_v1_TightLooseSkim/"

nCores                      = 5
outputDir                   = out_path
nEvents                     = -1
disableProgressBar          = False
justEndSequence             = False
#componentList               = [c for c in dataComponentDict.values() if "2016H" not in c.name] + componentDict.values() 
componentList               = [c for c in componentDict.values() if "WJets" in c.name and "HT" in c.name]
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

treeProducer            = TreeProducer("TreeProducer")#,listOfBranchesToKeep=branchesToKeep,branchesToAdd=branchesToAdd)

sequence = tl_rpv_skim_sequence
sequence.add(treeProducer)

endSequence = EndSequence(skipHadd=False)
endModuleOutputDir = out_path

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "SkimTree.root"
