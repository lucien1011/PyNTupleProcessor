from Core.ComponentList import *
from Core.Dataset import Dataset

#dataTreeDir     = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_ZXCRSelection/"
dataTreeDir     = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180806/SkimTree_Data80X_HIG-16-041-ZXCRSelection_v2/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2017_cmpList = ComponentList(
        [
            Component("Data_Run2016",dataTreeDir+"Data_Run2016_noDuplicates.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
Data_Run2017 = Dataset(
        "Data_Run2016",
        Data_Run2017_cmpList,
        isMC = False,
        )
