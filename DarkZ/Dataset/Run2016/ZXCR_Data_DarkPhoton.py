from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#dataTreeDir     = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_ZXCRSelection/"
#dataTreeDir     = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_HIG-16-041-ZXCRSelection_v2/"
#dataTreeDir     = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180905/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/"
#dataTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20181116/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/"
dataTreeDir      = system.getStoragePath()+"/lucien/Higgs/DarkZ-NTuple/20190115/SkimTree_DarkPhoton_ZX_Run2016Data_m4l70/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2016_cmpList = ComponentList(
        [
            Component("Data_Run2016",dataTreeDir+"Data_Run2016-03Feb2017_noDuplicates_FRWeight.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
Data_Run2016 = Dataset(
        "Data_Run2016",
        Data_Run2016_cmpList,
        isMC = False,
        )
