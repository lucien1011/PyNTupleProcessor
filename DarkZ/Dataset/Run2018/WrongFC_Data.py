from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2018_cmpList = ComponentList(
        [
            Component("Data_Run2016",
                system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20190402/SkimTree_DarkPhoton_WrongFC_Run2018Data_m4l70/Data_Run2018_noDuplicates_FRWeightFromVukasinWZRemoved.root",
                "passedEvents",inUFTier2=False),
        ]
        )
Data_Run2018 = Dataset(
        "WrongFC_Run2018",
        Data_Run2018_cmpList,
        isMC = False,
        )
