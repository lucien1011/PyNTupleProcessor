from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2016_cmpList = ComponentList(
        [
            Component("Data_Run2016",
                system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20190307/SkimTree_DarkPhoton_WrongFC_Run2017Data_m4l70/Data_Run2017-17Nov2017_noDuplicates.root",
                "passedEvents",inUFTier2=False),
        ]
        )
Data_Run2016 = Dataset(
        "WrongFC_Run2017",
        Data_Run2016_cmpList,
        isMC = False,
        )
