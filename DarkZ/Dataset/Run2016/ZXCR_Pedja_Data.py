from Core.ComponentList import *
from Core.Dataset import Dataset

inUFTier2       = False

# ____________________________________________________________________________________________________________________________________________ ||
PedjaData_Run2016_cmpList = ComponentList(
        [
            Component("PedjaData_Run2016","/raid/raid7/lucien/Higgs/DarkZ-NTuple/20180924/PedjaInput_rootfiles_MC80X_2lskim_M17_Feb21/Data_ZX_Run2017-03Feb2017_slimmedZX_FRWeight.root","selectedEvents",inUFTier2=inUFTier2),
        ]
        )
PedjaData_Run2016 = Dataset(
        "PedjaData_Run2016",
        PedjaData_Run2016_cmpList,
        isMC = False,
        )
