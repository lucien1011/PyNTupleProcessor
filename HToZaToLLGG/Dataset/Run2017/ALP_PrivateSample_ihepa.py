from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

import os

# ____________________________________________________________________________________________________________________________________________ ||
skimTreeDir_ALP         = "/raid/raid7/lucien/NanoAOD/ALP_PrivateSample/Oct19Prod/"
treePathInFile          = "Events"
inUFTier2               = False

# ____________________________________________________________________________________________________________________________________________ ||
# ALP_HToZa_M1
ALP_HToZa_M1_cmpList = ComponentList(
        [ 
            Component("ALP_HToZa_M1",os.path.join(skimTreeDir_ALP,"ALP_M1.root"),treePathInFile,inUFTier2=inUFTier2) 
        ]
        )

ALP_HToZa_M1 = Dataset(
        "ALP_HToZa_M1",
        ALP_HToZa_M1_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 1.,
        )

ALP_HToZa_M1.sumw = 0.
for cmp in ALP_HToZa_M1_cmpList:
    ALP_HToZa_M1.sumw += cmp.getSumWeightNanoAOD()

# ____________________________________________________________________________________________________________________________________________ ||
# ALP_HToZa_M5
ALP_HToZa_M5_cmpList = ComponentList(
        [ 
            Component("ALP_HToZa_M5",os.path.join(skimTreeDir_ALP,"ALP_M5.root"),treePathInFile,inUFTier2=inUFTier2) 
        ]
        )

ALP_HToZa_M5 = Dataset(
        "ALP_HToZa_M5",
        ALP_HToZa_M5_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 1.,
        )

ALP_HToZa_M5.sumw = 0.
for cmp in ALP_HToZa_M5_cmpList:
    ALP_HToZa_M5.sumw += cmp.getSumWeightNanoAOD()

# ____________________________________________________________________________________________________________________________________________ ||
# ALP_HToZa_M15
ALP_HToZa_M15_cmpList = ComponentList(
        [ 
            Component("ALP_HToZa_M15",os.path.join(skimTreeDir_ALP,"ALP_M15.root"),treePathInFile,inUFTier2=inUFTier2) 
        ]
        )

ALP_HToZa_M15 = Dataset(
        "ALP_HToZa_M15",
        ALP_HToZa_M15_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 1.,
        )

ALP_HToZa_M15.sumw = 0.
for cmp in ALP_HToZa_M15_cmpList:
    ALP_HToZa_M15.sumw += cmp.getSumWeightNanoAOD()

# ____________________________________________________________________________________________________________________________________________ ||
# ALP_HToZa_M30
ALP_HToZa_M30_cmpList = ComponentList(
        [ 
            Component("ALP_HToZa_M30",os.path.join(skimTreeDir_ALP,"ALP_M30.root"),treePathInFile,inUFTier2=inUFTier2) 
        ]
        )

ALP_HToZa_M30 = Dataset(
        "ALP_HToZa_M30",
        ALP_HToZa_M30_cmpList,
        isMC                = True,
        isSignal            = True,
        xs                  = 1.,
        )

ALP_HToZa_M30.sumw = 0.
for cmp in ALP_HToZa_M30_cmpList:
    ALP_HToZa_M30.sumw += cmp.getSumWeightNanoAOD()
