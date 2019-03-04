from Core.ComponentList import *
from Core.Dataset import Dataset

dataTreeDir      = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20181116/SkimTree_DarkPhoton_ZX_Run2017Data_m4l70/"
inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
Data_Run2017_cmpList = ComponentList(
        [
            Component("Data_Run2017",dataTreeDir+"Data_Run2017-17Nov2017_noDuplicates_FRWeightv2.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
Data_Run2017 = Dataset(
        "Data_Run2017",
        Data_Run2017_cmpList,
        isMC = False,
        )
