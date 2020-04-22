from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

import os

# ____________________________________________________________________________________________________________________________________________ ||
treePathInFile          = "Events"
inUFTier2               = False

# ____________________________________________________________________________________________________________________________________________ ||
# ZGGToLLGG
bkgSkimTreeDir_ZGGToLLGG = "/raid/raid7/lucien/NanoAOD/RunIIFall17NanoAOD/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/"

ZGGToLLGG_cmpList = ComponentList(
        [ 
            Component("ZGGToLLGG",os.path.join(bkgSkimTreeDir_ZGGToLLGG,"ZGGToLLGG_5f_TuneCP5_13TeV-amcatnlo-pythia8.root"),treePathInFile,inUFTier2=inUFTier2),
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
