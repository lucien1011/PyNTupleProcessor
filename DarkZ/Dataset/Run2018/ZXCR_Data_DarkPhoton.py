from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system

dataTreeDir      = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20190402/SkimTree_DarkPhoton_ZX_Run2018Data_m4l70/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2017_cmpList = ComponentList(
        [
            Component("Data_Run2018",dataTreeDir+"Data_Run2018_noDuplicates_FRWeightFromVukasinWZRemoved.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
Data_Run2017 = Dataset(
        "Data_Run2018",
        Data_Run2017_cmpList,
        isMC = False,
        )
