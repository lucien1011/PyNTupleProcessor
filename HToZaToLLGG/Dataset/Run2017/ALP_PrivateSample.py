from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

import os

# ____________________________________________________________________________________________________________________________________________ ||
treePathInFile          = "Events"
inUFTier2               = True

# ____________________________________________________________________________________________________________________________________________ ||
# ALP_HToZa_M1
skimTreeDir_ALP_M1 = "/cms/data/store/user/klo/ALP_HToZaTo2l2g/NANOAODSIM/ALP_HToZaTo2l2g_M1_GENSIM/NANOAODSIM-PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3/200203_140128/0000/"

ALP_HToZa_M1_cmpList = ComponentList(
        [ 
            Component("ALP_HToZa_M1",os.path.join(skimTreeDir_ALP_M1,"ALP_NANOAODSIM_%s.root"%i),treePathInFile,inUFTier2=inUFTier2) for i in range(1,98) 
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
