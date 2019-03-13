from Core.ComponentList import *
from Core.Dataset import Dataset

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2016_cmpList = ComponentList(
        [
            Component("Data_Run2016",
                "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190307/SkimTree_DarkPhoton_WrongFC_Run2016Data_m4l70/Data_Run2016-03Feb2017_4l.root",
                "passedEvents",inUFTier2=False),
        ]
        )
Data_Run2016 = Dataset(
        "WrongFC_Run2016",
        Data_Run2016_cmpList,
        isMC = False,
        )
