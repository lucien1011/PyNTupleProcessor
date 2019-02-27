from Core.ComponentList import *
from Core.Dataset import Dataset

dataTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190218/SkimTree_HToZdZd_ZX_Run2016Data_m4l70_noZCandRatioCut/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2016_cmpList = ComponentList(
        [
            Component("Data_Run2016",dataTreeDir+"Data_Run2016-2l_noDuplicates_FRWeight.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
Data_Run2016 = Dataset(
        "Data_Run2016",
        Data_Run2016_cmpList,
        isMC = False,
        )
