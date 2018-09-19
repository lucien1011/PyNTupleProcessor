# UF Framework specifics
from Core.Sequence import Sequence
from Core.OutputInfo import OutputInfo 
from Core.EndSequence import EndSequence

from Common.TreeProducer import TreeProducer

from RA5.Skimmer.BaselineSkimmer import BaselineSkimmer,NJetSkimmer,TreeSkimmer
from RA5.LeptonJetRecleaner.EventProducer import LeptonJetProducer 

from Config.BranchToAdd import branchesToAdd
from Config.BranchToKeep import branchesToKeep

from Core.Utils.LambdaFunc import LambdaFunc

import os,array

from DataMC.Heppy.Run2016.HaddData import * 
from DataMC.Heppy.Run2016.SampleDefinition import *

from NanoAOD.Producer.GenWeightCounter import *

out_path = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/Data_Run2016B_July18_v1_nJet2TightLep1_LeptonJetRecleaner/"

nCores = 5
outputDir = out_path
nEvents = -1
disableProgressBar = False
justEndSequence = False
#componentList = [TT_pow]
#componentList = [SyncMC]
for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = 35.9
    for component in dataset.componentList:
        component.maxEvents = nEvents

leptonJetProducer       = LeptonJetProducer("LeptonJetProducer","Run2016")
treeProducer            = TreeProducer("TreeProducer",listOfBranchesToKeep=branchesToKeep,branchesToAdd=branchesToAdd)
#baselineSkimmer         = BaselineSkimmer("SignalRegionSkimmer")
nJetSkimmer             = NJetSkimmer("SignalRegionSkimmer")
treeSkimmer             = TreeSkimmer("TreeSkimmer")
preskimCounter          = GenWeightCounter("GenWeightCounter",postfix="PreBaselineCut")
postskimCounter         = GenWeightCounter("GenWeightCounter",postfix="PostBaselineCut")

sequence = Sequence()
sequence.add(preskimCounter)
sequence.add(leptonJetProducer)
#sequence.add(nJetSkimmer)
sequence.add(treeSkimmer)
sequence.add(postskimCounter)
sequence.add(treeProducer)

endSequence = EndSequence(skipHadd=False)
endModuleOutputDir = out_path

outputInfo = OutputInfo("OutputInfo")
outputInfo.outputDir = outputDir
outputInfo.TFileName = "SkimTree.root"
