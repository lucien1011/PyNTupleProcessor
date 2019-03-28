from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system

dataTreeDir      = system.getStoragePath()+"/lucien/Higgs/HZZ4l/NTuple/ZPlusX/ZXCR/20190313_Run2017_ZXCR-Z1LSkim_LiteHZZTree/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2017_cmpList = ComponentList(
        [
            Component("Data_Run2017",dataTreeDir+"Data_Run2017-17Nov2017_noDuplicates.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
Data_Run2017 = Dataset(
        "Data_Run2017",
        Data_Run2017_cmpList,
        isMC = False,
        )
