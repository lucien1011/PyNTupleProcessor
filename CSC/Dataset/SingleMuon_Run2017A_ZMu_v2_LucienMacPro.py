from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight
import os

# ____________________________________________________________________________________________________________________________________________ ||
SingleMuon_Run2017A_ZMu_v2 = Dataset(
        "SingleMuon_Run2017A_ZMu_v2",
        ComponentList(
            [ 
                Component("SingleMuon_Run2017A_ZMu_v2","/Users/lucien/CMS/Misc/DUMMYFILENAME_1.root","cscRootMaker/Events",inUFTier2=False),
            ]
        ),
        isMC = False,
        )
