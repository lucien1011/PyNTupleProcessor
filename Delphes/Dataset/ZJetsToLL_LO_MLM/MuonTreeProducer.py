from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
import os

# ____________________________________________________________________________________________________________________________________________ ||
# 
ZJetsToLL_LO_MLM = Dataset(
        "ZJetsToLL_LO_MLM",
        ComponentList(
            [ 
                Component("ZJetsToLL_LO_MLM","/cmsuf/data/store/user/t2/users/klo/Delphes/ZJetsToLL_LO_MLM/2020-07-09/MuonTreeProducer/2020-07-09_MuonTreeProducer.root","LiteTree",inUFTier2=False),
            ]
        ),
        isMC                = True,
        xs                  = 1,
        )
ZJetsToLL_LO_MLM.sumw = 4899797.
