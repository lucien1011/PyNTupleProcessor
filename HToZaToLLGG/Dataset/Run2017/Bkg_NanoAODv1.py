from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

import os

# ____________________________________________________________________________________________________________________________________________ ||
treePathInFile          = "Events"
inUFTier2               = True

# ____________________________________________________________________________________________________________________________________________ ||
# ZGGToLLGG
bkgSkimTreeDir_ZGGToLLGG_1 = "/cms/data/store/mc/RunIIFall17NanoAOD/ZGGToLLGG_5f_TuneCP5_13TeV-amcatnlo-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/280000/"

ZGGToLLGG_cmpList = ComponentList(
        [ 
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG_1,"0A4048FC-5346-E911-9C77-90E2BA0FAFB4.root"),treePathInFile,inUFTier2=inUFTier2),
        ]
        )

ZGGToLLGG = Dataset(
        "ZGGToLLGG",
        ZGGToLLGG_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )

ZGGToLLGG.sumw = 0.
for cmp in ZGGToLLGG_cmpList:
    ZGGToLLGG.sumw += cmp.getSumWeightNanoAOD()

# ____________________________________________________________________________________________________________________________________________ ||
