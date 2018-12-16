from Core.ComponentList import *
from Core.Dataset import Dataset

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2016_cmpList = ComponentList(
        [
            Component("Data_Run2016",
                "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180920/SkimTree_WFC_Run2016Data_v1/Data_Run2016-03Feb2017_4l_1.root",
                "passedEvents",inUFTier2=False),
        ]
        )
Data_Run2016 = Dataset(
        "WrongFC_Run2016",
        Data_Run2016_cmpList,
        isMC = False,
        )
