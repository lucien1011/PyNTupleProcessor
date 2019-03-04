from Core.ComponentList import *
from Core.Dataset import Dataset

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2016_cmpList = ComponentList(
        [
            Component("Data_Run2016",
                "/raid/raid7/lucien/Higgs/HZZ4l/NTuple/ZPlusX/WrongFC/20181209/SkimTree_WrongFC_Run2016Data_v1/Data_Run2016-03Feb2017_4l_noDuplicates.root",
                "passedEvents",inUFTier2=False),
        ]
        )
Data_Run2016 = Dataset(
        "Run2016",
        Data_Run2016_cmpList,
        isMC = False,
        )
